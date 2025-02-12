import sys
sys.stdin = open("pang.txt", "r")

def pang():
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]  # n줄

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    maxv = 0

    for i in range(n):
        for j in range(m):
            sumv = arr[i][j] # 가운데 풍선의 값
            for di, dj in directions:
                for step in range(1, arr[i][j]+1): # sum v가 아래에서 계속 누적되니, 고정값인 arr[i][j]러 입력 !!
                    ni, nj = i + di * step, j + dj * step # 상하좌우로 가운데 풍선 값의 칸만큼 합산
                    if 0 <= ni < n and 0 <= nj < m:
                        sumv += arr[ni][nj]
            if sumv > maxv:
                maxv = sumv
    return maxv

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {pang()}')