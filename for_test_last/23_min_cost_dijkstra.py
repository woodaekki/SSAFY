from collections import deque

def dijkstra(x, y):
    queue = deque()
    queue.append((x, y))  # 시작점 추가
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 거리(연료 소비량)를 저장하는 배열, 초기값은 무한대
    dist = [[float("inf")] * N for _ in range(N)]
    dist[x][y] = 0 # 시작 위치의 연료 소비량은 0으로 설정

    while queue:
        x, y = queue.popleft()

        for di, dj in directions:
            ni, nj = x + di, y + dj
            if 0 <= ni < N and 0 <= nj < N:
                # 낮거나 같은 곳으로 이동할 때는 기본 연료 소비량 1만 반영
                # 높은 곳으로 이동할 때는 높이 차이 + 1 만큼
                diff = max(arr[ni][nj] - arr[x][y], 0) + 1  # (x, y) 기준으로 수정
                new_cost = dist[x][y] + diff  # 현재 비용 + 이동 비용

                if dist[ni][nj] > new_cost:  # 기존보다 연료 소비량이 적다면 업데이트
                    dist[ni][nj] = new_cost # 최적의 연료 소비량 갱신
                    queue.append((ni, nj))  # 그 좌표 큐에 추가

    return dist

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra(0, 0)
    print(f'#{t} {result[N - 1][N - 1]}')