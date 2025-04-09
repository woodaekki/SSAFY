# import sys
# sys.stdin = open("1.txt", "r")


from collections import deque

# 매년 녹는 양 계산
def melt():
    melt_amount = [[0]*M for _ in range(N)] # 각 칸이 얼마나 녹아야 하는지 저장할 배열
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 각 칸의 인접한 바다(0) 개수 세기
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:  # 얼음 있는 칸에
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 0: # 사방에 0있으면
                        melt_amount[i][j] += 1

    # 빙산 녹이기 (단, 최소 0)
    for i in range(N):
        for j in range(M):
            graph[i][j] = max(0, graph[i][j] - melt_amount[i][j])

# 빙산 덩어리 구역 세기
def icebergs(graph):
    visited = [[0]*M for _ in range(N)]
    cnt = 0  # 빙산 덩어리 구역 개수

    for i in range(N):
        for j in range(M): # 아직 칸이 있는데 방문 안했으면 bfs로 보내서 방문 처리
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1

    return cnt

def bfs(x, y, visited):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        a, b = queue.popleft()
        for dx, dy in directions:
            c, d = a + dx, b + dy
            if 0 <= c < N and 0 <= d < M:
                if graph[c][d] > 0 and not visited[c][d]:
                    visited[c][d] = 1
                    queue.append((c, d))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

year = 0
while True:
    curr_cnt = icebergs(graph)  # 현재 빙산 덩어리 개수 세기
    if curr_cnt == 0:  # 빙산 다 녹았으면
        print(0)
        break
    if curr_cnt >= 2:  # 두 덩어리 이상
        print(year)
        break

    melt()  # 빙산 녹이기
    year += 1