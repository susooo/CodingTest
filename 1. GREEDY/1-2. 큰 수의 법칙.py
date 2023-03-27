# 큰 수의 법칙 : 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단 특정한 인덱스에 해당하는 숫자가 연속해서 K번을 초과하여 더해질 수 없다.

"""
[입력예시]
5 8 3
2 4 5 4 6

[출력예시]
46
"""

n, m, k = map(int, input().split())  # 배열의 크기 n, 숫자가 더해지는 횟수 m, 더해질 수 있는 최대 횟수 k
n_list = sorted(map(int, input().split()))  # 입력받은 다양한 숫자로 이루어진 배열을 오름차순으로 정렬

first = n_list[-1]  # 배열 안 가장 큰 수
second = n_list[-2]  # 배열 안 두번째로 큰 수
count = 0  # k를 넘지 않도록 하기 위한 장치
result = 0  # 큰 수의 법칙 결과

for _ in range(m):
    if count < k:  # k를 넘지 않는한 가장 큰 수 더하기
        result += first
        count += 1
    else:  # k를 넘는 경우 두번째로 큰 수 더하기
        result += second
        count = 0  #k reset
print(result)