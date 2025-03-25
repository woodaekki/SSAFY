import sys
sys.stdin = open("maze1.txt", "r")

from collections import deque

# 1은 벽 / 0은 길 / 3은 도착점
def bfs(start, arr):
    visited = [[0] * 16 for _ in range(16)]  
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  

    # 시작점 방문
    queue = deque()
    queue.append((start[0], start[1]))
    visited[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()
        
        # 도착점에 도달하면 1 반환
        if arr[x][y] == 3:
            return 1
        
        for di, dj in directions:
            ni, nj = x + di, y + dj
            # 벽을 제외한 방문하지 않은 곳이라면 방문하기 
            if 0 <= ni < 16 and 0 <= nj < 16 and arr[ni][nj] != 1 and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = 1

    return 0

T = 10
for t in range(1, T + 1):
    tc = int(input()) 
    arr = [list(map(int, input())) for _ in range(16)]  
    
    s = (1, 1)  # 시작점
    
    result = bfs(s, arr)
    print(f'#{tc} {result}')


