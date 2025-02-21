import sys
sys.stdin = open("2178.txt", "r")

from collections import deque

def bfs(x, y):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 시작점 방문처리
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    cnt = 1 # 지나야하는 최소 칸 수, 시작점 방문했으니까 1로 시작

    while queue:
        x, y = queue.popleft() # 선입된걸 빼서
        for di, dj in directions:
            ni, nj = x + di, y + dj
            # 경계에서 벗어나지 않았는데, 1이고 방문하지 않았으면
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    print(cnt)


n, m = list(map(int, input().split()))
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(m)] # 방문목록 초기화
for i in range(n):
    for j in range(m):
        # 미로에서 1인데, 방문하지 않았으면
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j) # bfs 호출해서 인접한 1을 쭉 따라간다.


