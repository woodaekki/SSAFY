map_data = [
    ['G', 'G', 'R', 'G', 'G', 'G', 'W', 'G', 'G', 'X'],  # 우상단 포탑 (X)
    ['G', 'W', 'R', 'G', 'G', 'R', 'W', 'R', 'G', 'G'],
    ['G', 'G', 'G', 'G', 'R', 'G', 'G', 'R', 'G', 'G'],
    ['G', 'R', 'R', 'G', 'G', 'W', 'G', 'G', 'R', 'G'],
    ['G', 'G', 'W', 'W', 'G', 'R', 'R', 'G', 'G', 'G'],
    ['G', 'G', 'G', 'R', 'G', 'G', 'W', 'G', 'R', 'G'],
    ['R', 'G', 'R', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'G', 'W', 'G', 'R', 'G', 'R', 'W', 'G', 'G'],
    ['G', 'G', 'G', 'G', 'G', 'R', 'G', 'G', 'W', 'G'],
    ['A', 'G', 'G', 'R', 'G', 'G', 'G', 'G', 'G', 'G'],  # 좌하단 전차 (A)
]

from collections import deque


D= {'U': (-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
R = {(-1,0): 'U', (1,0):'D', (0, -1):'L', (0,1):'R'}

def fire(y, x, w, h, target_tank):       # 3칸거리일때 쏘는 함수
    for k, (dy,dx) in D.items():
        for i in range(1,4):
            ny, nx = y + dy*i, x+dx *i
            if 0<= nx < w and 0<= ny < h:
                if (ny, nx) == target_tank:
                    return f'{k} F'
                if map_data[ny][nx] != 'G':
                    break
    return None


def bfs(start_tank, target_tank, h, w): #빈 리스트 만들어서 bsf 쓴 함수 오로지 G일때만 신경씀
    q= deque([(start_tank, [])])
    visited = set([start_tank])
    target = []
    for dx, dy in D.values():
        tx, ty = target_tank[0] + dx, target_tank[1] + dy
        if 0<= tx < h and 0<= ty < w and map_data[tx][ty] == 'G':
            target.append((tx, ty))

    while q:
        (x, y), path = q.popleft()
        if (x, y) in target:
            return path

        for dx, dy in D.values():
            nx, ny = x+dx, y+dy
            if 0<= nx < h and 0<= ny < w:
                if map_data[nx][ny] == 'G' and (nx, ny) not in visited:
                    visited.add((nx,ny))
                    q.append(((nx,ny), path + [R[(dx, dy)] + ' A']))
    return ['S']


h, w = len(map_data), len(map_data[0])
start_tank = target_tank = None
for row in range(h):                        #내 위치랑 포탑위치 찾는 코드
    for col in range(w):
        if map_data[row][col] == 'A':
            start_tank = (row, col)
        if map_data[row][col] == 'X':
            target_tank = (row, col)

output = fire(start_tank[0], start_tank[1], w, h, target_tank) or bfs(start_tank, target_tank, h, w)[0]