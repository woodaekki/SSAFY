import sys
sys.stdin = open("fly3.txt", "r")

def fly3():
    n, m = list(map(int, input().split())) # n x m
    arr = [list(map(int, input().split())) for _ in range(n)]  # n줄

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    maxv = 0

    # +자 분사
    for i in range(n):
        for j in range(m):
            sumv = arr[i][j] # 현재 위치
            for di, dj in directions:
                for step in range(1, arr[i][j] + 1):
                    ni, nj = di + i*step, dj + j*step # 현재 위치에서 step 칸만큼 분사
            if sumv > maxv: # 최대 퇴치의 경우 저장
                maxv = sumv

    # x자 분자
    sumv2 = maxv2 = 0
    for i in range(n):
        for j in range(m):
            sumv2 += arr[i][i]
            sumv2 += arr[i][j-1]
            if sumv2 > maxv2:
                maxv2 = sumv2

    sumv3 = maxv
    if maxv2 > sumv3:
        sumv3 = maxv2

    return sumv3

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {fly3()}')