from collections import deque

NICKNAME = "테스트"
HOST = "127.0.0.1"
PORT = 8747
socket = None
bytes_ = bytearray(1024)
map_data = []  # 맵 정보 (2차원 리스트 형태)
allies = {}  # 키: str, 값: 리스트[str]
enemies = {}  # 키: str, 값: 리스트[str]
codes = []  # 암호문 정보 (리스트 형태)

game_data = '''10 10 3 3 1
G R R G T G G R G X
G R R G T R G G G G
G R R G R R R G R R
F A G G G G R G G G
G R T T R G R G E1 G
G G T T R G G G G G
R G G G G R E2 R G R
G G R W W W G G G G
G G R W W W R R R G
H G G G A1 G G G G G
A 100 R 1 1
A1 10
H 10
E1 10
E2 10
X 10
AKWNSDN
'''


# map_data에서 target을 찾는 함수
def find_position(map_data, target):
    for r, row in enumerate(map_data):
        for c, val in enumerate(row):
            if val == target:
                return r, c
    return None


def bfs_shortest_path(map_data, start, goal):
    rows, cols = len(map_data), len(map_data[0])
    visited = [[False] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]

    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    # 방향: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()

        if (r, c) == goal:
            # 경로 재구성
            path = []
            while (r, c) != start:
                path.append((r, c))
                r, c = parent[r][c]
            path.append(start)
            return path[::-1]  # 시작 -> 목표 순서로 뒤집기

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and (map_data[nr][nc] == 'G' or (nr, nc) == goal):
                    visited[nr][nc] = True
                    parent[nr][nc] = (r, c)
                    queue.append((nr, nc))

    return None  # 도달 불가


def parse_data(input_data):
    game_data = input_data.split('\n')
    # 1. 맵 및 시작 위치, 암호문 수
    rows, cols, num_allies, num_enemies, num_codes = map(int, game_data[0].split())
    # 2. 맵 데이터
    global map_data
    map_data = [line.split() for line in game_data[1:1 + rows]]

    # 3. 아군 정보
    ally_lines = game_data[1 + rows:1 + rows + num_allies]
    allies: Dict[str, Dict] = {}

    for line in ally_lines:
        parts = line.split()
        name = parts[0]
        if name == "A":  # 본인
            allies[name] = {
                'type': 'self',
                'hp': int(parts[1]),
                'direction': parts[2],
                'normal_shells': int(parts[3]),
                'mega_shells': int(parts[4])
            }
        else:  # 다른 아군
            allies[name] = {
                'type': 'tank' if name.startswith('A') else 'turret',
                'hp': int(parts[1])
            }
    print(allies)
    # 4. 적군 정보
    enemy_start = 1 + rows + num_allies
    enemy_lines = game_data[enemy_start:enemy_start + num_enemies]
    enemies: Dict[str, Dict] = {}

    for line in enemy_lines:
        parts = line.split()
        name = parts[0]
        enemies[name] = {
            'type': 'tank' if name.startswith('E') else 'turret',
            'hp': int(parts[1])
        }
    print(enemies)
    # 5. 암호문 정보
    code_start = enemy_start + num_enemies
    codes: List[str] = game_data[code_start:code_start + num_codes]
    print(codes)

# 4. 암호문

# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(미 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:
    # 자기 차례가 되어 받은 게임정보 파싱
    parse_data(game_data)
    # 1. 시작/목표 위치 찾기
    start_pos = find_position(map_data, 'A')
    goal_pos = find_position(map_data, 'X')

    # 2. 최단경로 탐색
    path = bfs_shortest_path(map_data, start_pos, goal_pos)

    if path is None:
        goal_pos = find_position(map_data, 'Y')
