from collections import deque

def bfs(n, start, end): 
    directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    visited = [[0] * n for _ in range(n)]
    
    # 시작점과 도착점이 같으면 0 반환
    if start == end:
        return 0
        
    # 시작점 방문 
    queue = deque()
    queue.append((start[0], start[1])) # x, y
    visited[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()
        for di, dj in directions:
            ni, nj = x+di, y+dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = visited[x][y] +1 # 최소 거리 

                # 목적지에 도착하면 이동 횟수 반환
                if (ni, nj) == tuple(end):
                    return visited[ni][nj] - 1            
    

T = int(input())
for _ in range(T):
    n = int(input()) # n x n 배열 
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))
    
    result = bfs(n, before, after)
    print(result)