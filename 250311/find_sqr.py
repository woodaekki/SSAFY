def bfs(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 시작점 방문 처리
    queue = []
    queue.append((x, y))
    visited[x][y] = 1
    cnt = 1

    while queue:
        x, y = queue.pop(0)
        for di, dj in directions:
            ni, nj = x + di, y + dj
            # 경계에서 벗어나지 않았고, 1인데 방문하지 않았으면 방문 처리 후, 카운트 1 증가
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    found = False
    max_cnt = -1
    # 제일 처음 나온 1을 찾아서 호출
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                result = bfs(i, j)
                # 최대 1 개수 갱신
                max_cnt = max(max_cnt, result)
    print(f'#{t} {max_cnt}')