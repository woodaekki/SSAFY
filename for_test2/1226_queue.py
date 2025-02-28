import sys
sys.stdin = open("maze.txt", "r")

from collections import deque

def bfs(x, y):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 출발점 방문 처리
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for di, dj in directions:
            ni, nj = x + di, y + dj
            # 경계 내에 있고 벽이 아닌데 방문하지 않은 경우
            if 0 <= ni < 16 and 0 <= nj < 16 and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1
                # 도착점에 다다르면 1반환
                if (ni, nj) == end:
                    return 1
    return 0

T = 10
for t in range(1, T+1):
    tc = int(input())  # 테스트 케이스 번호 (사용 안 함)
    arr = [list(map(int, input().split())) for _ in range(16)]  # 16x16 지도 입력
    visited = [[0]*16 for _ in range(16)]  # 방문목록 생성
    start = (1,1)  # 출발점 (1,1) 위치
    end = (13,13)  # 도착점 (13,13) 위치

    # 출발점이 2인 경우에만 시작
    if start == 2:
        result = bfs(start)  # bfs 함수 호출
        print(f'#{t} {result}')
