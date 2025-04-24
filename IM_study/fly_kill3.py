import sys
sys.stdin = open("1.txt", "r")

def solve():
    max_sum = float('-inf')
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    # + 분사
    for i in range(n):
        for j in range(n):
            mid = arr[i][j]
            for di, dj in directions:
                for k in range(1, m):
                    ni, nj = i+di*k, j+dj*k
                    if 0<=ni<n and 0<=nj<n:
                        mid += arr[ni][nj]
            max_sum = max(max_sum, mid)

    max_sum2 = float('-inf')
    directions2 = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    # x 분사
    for i in range(n):
        for j in range(n):
            mid2 = arr[i][j]
            for di, dj in directions2:
                for k in range(1, m):
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < n and 0 <= nj < n:
                        mid2 += arr[ni][nj]
            max_sum2 = max(max_sum2, mid2)
    return max(max_sum, max_sum2)

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = solve()
    print(f'#{t} {result}')