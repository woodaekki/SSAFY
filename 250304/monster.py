def dfs():
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(n):
        for j in range(n):
            # 괴물을 발견한 순간 벽이 나올때까지 광선 쏘기
            if arr[i][j] == 2:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 1 and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        ni += di
                        nj += dj

    # 안전구역 = 광선 닿은 구간, 벽, 괴물있는 곳 제외
    cnt = 0
    for a in range(n):
        for b in range(n):
            if arr[a][b] != 1 and arr[a][b] != 2 and visited[a][b] != 1:
                cnt += 1
    return cnt


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    result = dfs()
    print(f'#{t} {result}')