import sys
sys.stdin = open("maze.txt", "r")

from collections import deque

def bfs(x, y):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 출발점 방문 처리
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for di, dj in directions:
            ni, nj = x+di, y+dj
            # 경계 내에 있고 벽이 아닌데 방문하지 않은 경우
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj]!=1 and visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = 1
                # 도착점에 다다르면 1반환
                if (ni,nj) == end:
                    return 1
    return 0

T = 10
for t in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)] # 방문목록 생성 
    start_i, start_j = 1, 1
    end = (13, 13)

    # 출발점 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                result = bfs(i, j)
    print(f'#{t} {result}')

