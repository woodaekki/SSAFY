import socket
from collections import deque

# 서버 접속 정보
HOST = '127.0.0.1'
PORT = 8747
sock = socket.socket()

# 방향 정의
D = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
R = {(-1, 0): 'U', (1, 0): 'D', (0, -1): 'L', (0, 1): 'R'}

# 초기 연결 (닉네임 전달)
def init(nickname):
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}')
        sock.connect((HOST, PORT))
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}'
        return submit(init_command)
    except Exception as e:
        print('[ERROR] Failed to connect.')
        print(e)

# 명령어 전송 및 응답 수신
def submit(string_to_send):
    try:
        sock.send((string_to_send + ' ').encode('utf-8'))
        return sock.recv(2048).decode('utf-8').strip()
    except Exception as e:
        print('[ERROR] Submit failed.')
    return None

# 소켓 연결 종료
def close():
    try:
        if sock is not None: sock.close()
        print('[STATUS] Connection closed')
    except Exception as e:
        print('[ERROR] Connection error.')

# 최단 경로 탐색 (BFS)
def bfs(start, target, h, w, map_data):
    q = deque([(start, [])])
    visited = set([start])
    goal_adj = []

    # 포탑(X) 주변 도착 가능한 G 좌표 저장
    for dx, dy in D.values():
        nx, ny = target[0] + dx, target[1] + dy
        if 0 <= nx < h and 0 <= ny < w and map_data[nx][ny] == 'G':
            goal_adj.append((nx, ny))

    # BFS 탐색
    while q:
        (x, y), path = q.popleft()
        if (x, y) in goal_adj:
            return path, (x, y)  # 경로와 마지막 위치 리턴
        for dx, dy in D.values():
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and map_data[nx][ny] == 'G' and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(((nx, ny), path + [R[(dx, dy)] + ' A']))

# 사거리 내에 X가 보이면 공격 명령 리턴
def fire(x, y, target, h, w, map_data):
    for dir_key, (dx, dy) in D.items():
        for i in range(1, 4):
            nx, ny = x + dx * i, y + dy * i
            if 0 <= nx < h and 0 <= ny < w:
                if (nx, ny) == target:
                    return dir_key + ' F'
                if map_data[nx][ny] != 'G':
                    break

# 닉네임 설정 후 INIT
NICKNAME = '통신테스트'
game_data = init(NICKNAME)

# 메인 루프: 서버와 통신하며 명령 처리
while game_data:
    print(f'{game_data}\n')

    # 맵 정보 수신 시 처리
    if game_data.startswith('<stage'):
        lines = game_data.splitlines()
        dims = list(map(int, lines[1].split()))
        h, w = dims[0], dims[1]
        map_data = [line.split() for line in lines[2:2 + h]]

        # A(시작), X(포탑) 위치 찾기
        for i in range(h):
            for j in range(w):
                if map_data[i][j] == 'A': start = (i, j)
                if map_data[i][j] == 'X': target = (i, j)

        # 최단 경로 계산 및 이동 명령
        path, last_pos = bfs(start, target, h, w, map_data)
        actions = path.copy()

        # 포탑 사거리 진입 시 공격 명령 추가
        fire_cmd = fire(last_pos[0], last_pos[1], target, h, w, map_data)
        if fire_cmd: actions.append(fire_cmd)

        # 커맨드 하나씩 서버에 전송
        for cmd in actions:
            game_data = submit(cmd)
            print(f'{cmd} -> {game_data}')

    else:
        game_data = submit('A')  # 기본 대기 혹은 다음 턴 명령

    break  # 테스트용 1회 실행. 실제 게임에서는 제거

# 통신 종료
close()