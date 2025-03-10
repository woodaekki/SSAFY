from collections import deque
def bfs(r, c):
    dy =
    dx =
    # 지하 터널 종류
    types = {
        1: [1, 1, 1, 1],
        2: [1, 1, 0, 0],
        3: [0, 0, 1, 1],
        4: [1, 0, 0, 1],
        5: [0, 1, 0, 1],
        6: [0, 1, 1, 0],
        7: [1, 0, 1, 0]
    }
    # 시작점 방문 처리
    dq = deque()
    dq.append((r, c))
    visited[r][c] = 1

    while dq:
        curr_y, curr_x = dq.popleft()
        directions = types[arr[curr_y][curr_x]]
        for i in range(4):
            # 출구가 안 열려있는 경우 continue
            if directions[i] == 0:
                continue
            new_y = curr_y + dy[i]
            new_x = curr_x = dx[i]

            # 범위 밖으로 넘어가면 pass
            if
            # 이미 방문했다면 pass

            # 못가면 pass







T = int(input())
for t in range(1, T + 1):
    n, m, r, c, l = map(int, input().split()) # 가로, 세로, 맨홀의 세로, 맨홀의 가로, 소요시간
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)] # 특정 좌표까지 몇 시간이 걸렸는지 기록
    result = bfs(r, c)
    print(f'#{t} {result}')