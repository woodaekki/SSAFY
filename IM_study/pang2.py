import sys
sys.stdin = open("1.txt", "r")

def solve():
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)] # 상하좌우
    maxv = float('-inf')
    minv = float('inf')
    for i in range(n):
        for j in range(n):
            mid = arr[i][j]
            for di, dj in directions:
                for k in range(1, n):
                    ni, nj = i+di*k, j+dj*k
                    if 0<= ni < n and 0<= nj < n:
                        mid += arr[ni][nj]
            maxv = max(maxv, mid)
            minv = min(minv, mid)
    return maxv - minv


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = solve()
    print(f'#{t} {result}')