# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램(최소 봉지 개수)

import sys

n = int(sys.stdin.readline())

for i in range(n//5,-1,-1):
    # 5의 배수
    if n-(5*i) == 0:
        answer = n//5
        break
    # 5와 3 조합
    elif ((n-(5*i))%3) == 0:
        answer = i+(n-(5*i))//3
        break
    # 그 외
    else:
        answer = -1

print(answer)