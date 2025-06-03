def bfs(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
 
    # 시작점 방문 
    queue = []
    queue.append((x, y))
    visited[x][y] = 1
    cnt = 1
 
    while queue:
        x, y = queue.pop(0)
        for di, dj in directions:
            ni, nj = x+di, y+dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = 1
                queue.append((ni, nj))
                cnt += 1
    return cnt
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
 
    max_cnt = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                max_cnt = max(max_cnt, bfs(i, j))
    print(f'#{t} {max_cnt}')