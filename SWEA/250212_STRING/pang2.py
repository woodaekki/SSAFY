def pang():
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]  # n줄
 
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    maxv = 0
 
    for i in range(n):
        for j in range(m):
            sumv = arr[i][j]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    sumv += arr[ni][nj]
            if sumv > maxv:
                maxv = sumv
    return maxv
 
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {pang()}')