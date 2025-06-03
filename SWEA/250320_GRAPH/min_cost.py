from collections import deque
 
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
 
    dist = [[float('inf')] * n for _ in range(n)]
    dist[x][y] = 0
 
    while queue:
        x, y = queue.popleft()
        for di, dj in directions:
            ni, nj = x+di, y+dj
            if 0<=ni<n and 0<=nj<n:
                diff = max(arr[ni][nj]-arr[x][y], 0) + 1 # 인접지역 갈시 기본 1 연료 증가
                new_cost = diff + dist[x][y]
                if new_cost < dist[ni][nj]:
                    dist[ni][nj] = new_cost
                    queue.append((ni, nj))
    return dist[n-1][n-1]
 
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
 
    result = bfs(0, 0)
    print(f'#{t} {result}')