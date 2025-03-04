def pang():
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    maxv = -999999999999999
    for i in range(n):
        for j in range(m):
            sumv = arr[i][j]
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < n:
                    sumv += arr[ni][nj]
            if sumv > maxv:
                maxv = sumv
    return maxv

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = pang()
    print(f'#{t} {result}')
