import sys
sys.stdin = open("supply.txt", "r")

from collections import deque

def dijkstra(x, y):
    # 시작점 큐에 넣기
    queue = deque()
    queue.append((x, y))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    time = [[float("inf")] * 100 for _ in range(100)]  # 누적 복구 시간 저장 리스트
    time[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for di, dj in directions:
            ni, nj = x + di, y + dj
            if 0 <= ni < n and 0 <= nj < n:
                new_time = time[x][y] + arr[ni][nj]  # 누적 시간 + 이동 시간
                if new_time < time[ni][nj]:  # 이동할 시간보다 더 적은 복구 시간이면 업데이트
                    time[ni][nj] = new_time
                    queue.append((ni, nj))

    return time  # 도착점의 최소 복구 시간 반환

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    result = dijkstra(0, 0)
    print(f"#{t} {result[n-1][n-1]}")