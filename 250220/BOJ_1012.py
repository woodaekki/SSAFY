def dfs(j,i):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    stack = []
    stack.append((j,i))
    visited[j][i] = True

    while stack:
        i, j = stack.pop(-1)

        # 인접한 상하좌우 배추밭 탐색
        for di, dj in directions:
            ni, nj = i+di, j+dj
            # 범위 벗어나지 않았고, 배추가 있는데, 방문하지 않았으면
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == False:
                visited[ni][nj] = True # 방문 처리하고
                stack.append((ni, nj)) # 스택에 넣기
    return True

T = int(input())
for t in range(1, T+1):
    m, n, k = list(map(int, input().split())) # 가로, 세로, 배추 총 개수
    arr = [[0] * m for _ in range(n)]
    visited = [[False]*m for _ in range(n)] # 방문 목록 저장
    cnt = 0
    for _ in range(k):
        i, j = list(map(int, input().split())) # 배추가 저장된 가로 세로 좌표
        arr[j][i] = 1 # 배추 위치 저장

    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1 and visited[x][y] == False:
                if dfs(x, y):
                    cnt += 1

    print(cnt)