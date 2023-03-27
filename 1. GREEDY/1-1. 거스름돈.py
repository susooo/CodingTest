# 거스름돈이 N원일 때 줘야할 동전의 최소 개수 구하기

"""
[입력예시]
1260

[출력예시]
6
"""

n = int(input())
coins = [500, 100, 50, 10]  # 큰 단위 동전부터 거슬러 주기
count = 0

for coin in coins:
    count += (n // coin)  # 해당 단위 동전으로 줄 수 있는 최대 개수
    n %= coin  # 해당 단위 동전으로 나눠주고 남은 금액
print(count)
