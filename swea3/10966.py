from collections import deque

def bfs(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 시작점 저장
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    cnt = 1 # 현재 사각 영역
    while queue:
        x, y = queue.popleft()
        for di, dj in directions:
            ni, nj = x+di, y+dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = 1
                queue.append((ni, nj))
                cnt += 1

    return cnt
    
T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)] # 방문 목록 생성

    max_cnt = 0 # 최대 사각영역 저장

    # 처음 1이 나타나는 영역 찾는 순간 bfs 호출하기 
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:  # 방문하지 않은 1인 경우
                max_cnt = max(max_cnt, bfs(i, j))
    print(f'#{t} {max_cnt}')