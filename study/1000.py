from collections import deque

# 방향 이동을 위한 딕셔너리 (상, 하, 좌, 우)
D = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

# 반대로, 방향 벡터를 문자로 바꾸기 위한 딕셔너리
R = {(-1, 0): 'U', (1, 0): 'D', (0, -1): 'L', (0, 1): 'R'}

# 발사 함수: 현재 위치(x,y)에서 target_tank를 향해 포탄을 발사할 수 있는지 확인
def fire(x, y, target_tank, h, w):
    for ke, xy in D.items():  # 네 방향으로 반복
        for i in range(1, 4):  # 최대 3칸까지 탐색
            nx, ny = x + xy[0] * i, y + xy[1] * i  # 이동한 좌표 계산
            if 0 <= nx < h and 0 <= ny < w:
                if (nx, ny) == target_tank:  # 목표 탱크를 발견한 경우
                    return f'{ke} F'  # 해당 방향으로 발사
                if map_data[nx][ny] != 'G':  # 중간에 장애물이 있으면 탐색 종료
                    break

# BFS 함수: 시작 탱크에서 목표 탱크 근처로 가기 위한 경로를 찾음
def bfs(start_tank, target_tank, h, w):
    q = deque([(start_tank, [])])  # 시작 위치와 경로 저장
    visited = set([start_tank])  # 방문한 위치 저장
    target = []
    # 목표 탱크 주변 4방향 중 이동 가능한 위치를 저장
    for dx, dy in D.values():
        nx, ny = target_tank[0] + dx, target_tank[1] + dy
        if 0 <= nx < h and 0 <= ny < w and map_data[nx][ny] == 'G':
            target.append((nx, ny))
    while q:
        (x, y), path = q.popleft()
        # 목표 근처에 도달하면 경로 반환
        if (x, y) in target:
            return path
        # 4방향으로 이동 가능한 경우 큐에 추가
        for dx, dy in D.values():
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and 0 <= nx < h and 0 <= ny < w and map_data[nx][ny] == 'G':
                visited.add((nx, ny))
                q.append(((nx, ny), path + [R[(dx, dy)] + ' A']))  # 이동 명령 추가

# 맵 설정
map_data = [['G', 'G', 'G', 'X'],
            ['G', 'R', 'G', 'G'],
            ['A', 'G', 'G', 'G']]

# 맵 크기 계산
h, w = len(map_data), len(map_data[0])
print(h, w)

# 시작 탱크(A)와 목표 탱크(X)의 위치를 찾기
for i in range(h):
    for j in range(w):
        if map_data[i][j] == 'A':
            start_tank = (i, j)
        elif map_data[i][j] == 'X':
            target_tank = (i, j)

# BFS 경로 중 첫 명령 출력
print(bfs(start_tank, target_tank, h, w)[0])

# 발사 가능하면 방향과 함께 발사 명령 출력
fire(start_tank[0], start_tank[1], target_tank, h, w)
