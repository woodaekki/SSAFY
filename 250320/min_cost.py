import sys
sys.stdin = open("min_cost.txt", "r")

from collections import deque

def dijkstra(x, y):
    queue = deque()
    queue.append((x, y))  # 시작점 추가
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    dist = [[float("inf")] * N for _ in range(N)]
    dist[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for di, dj in directions:
            ni, nj = x + di, y + dj
            if 0 <= ni < N and 0 <= nj < N:
                diff = max(arr[ni][nj] - arr[x][y], 0) + 1  # (x, y) 기준으로 수정
                new_cost = dist[x][y] + diff  # 현재 비용 + 이동 비용

                if dist[ni][nj] > new_cost:  # 더 적은 연료 소비량이면 업데이트
                    dist[ni][nj] = new_cost
                    queue.append((ni, nj))  # 큐에 추가

    return dist


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra(0, 0)
    print(f'#{t} {result[N - 1][N - 1]}')