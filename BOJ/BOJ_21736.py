from collections import deque

def bfs(x, y):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = 0

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for di, dj in directions:
            ni, nj = x + di, y + dj
            if 0 <= ni < n and 0 <= nj < m and (arr[ni][nj] == 'O' or arr[ni][nj] == 'P') and not visited[ni][nj]:
                visited[ni][nj] = 1
                queue.append((ni, nj))
                if arr[ni][nj] == 'P':
                    cnt += 1
    
    # 아무도 만나지 못한 경우 
    if cnt == 0:
        return 'TT' 
    return cnt 

n, m = list(map(int, input().split()))
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I': # 도연이 위치
            result = bfs(i, j)
            print(result)