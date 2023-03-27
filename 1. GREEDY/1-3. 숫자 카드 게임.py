# nxm 행렬에서 각 행에서 가장 작은 수를 뽑고 그 수들 중에 가장 큰 수 뽑기

"""
[입력예시]
2 4
7 3 1 8
3 3 3 4

[출력예시]
3
"""

n, m = map(int, input().split())
small_list = []  # 각 행에서 가장 작은 수 담기 위한 리스트
for _ in range(n):
    row = list(map(int, input().split()))
    small_list.append(min(row))  # 각 행에서 가장 작은 수 담기
print(max(small_list))  # 리스트에서 가장 큰 수 뽑기
