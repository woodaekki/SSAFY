def dfs(x, y):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited  = [[0] * n for _ in range(n)]

    stack = []
    stack.append((x, y))
    visited[x][y] = 1

    while stack:
        x, y = stack.pop(-1)
        for di, dj in directions:
            ni, nj = x+di, y+dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 1 and not visited[ni][nj]:
                stack.append((ni, nj))
                visited[ni][nj] = 1
                if arr[ni][nj] == 3:
                    return 1
    return 0

T = int(input())
for t in range(1, T + 1):
    n = int(input())  # n x n 배열
    arr = [list(map(int, input().strip())) for _ in range(n)]  

    visited = [[0] * n for _ in range(n)]  

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                start_x, start_y = i, j
                break  

    result = dfs(start_x, start_y)
    print(f'#{t} {result}')