import sys
sys.stdin = open("2.txt", "r")

from collections import deque

def bfs(start_i, start_j, k):
    global min_cnt
    queue = deque()
    queue.append((start_i, start_j, 0, 0, k)) # 시작위치, 현재 방향, 조작횟수, 남은 나무횟수
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
    visited = set()  # 방문 상태 기록

    while queue:
        x, y, dir, cnt, cut = queue.popleft()
        # 가지 치기
        if cnt >= min_cnt:
            continue
        # (시간 초과 해결 위해 지선생님께 여쭌 부분)
        # 현재위치, 현재방향, 나무베기 제한횟수가 완전히 일치한다면
        # 이미 탐색한적 있는 경로이므로 스톱
        if (x, y, dir, cut) in visited:
            continue
        visited.add((x, y, dir, cut)) # 그리고 저장

        if arr[x][y] == 'Y':
            min_cnt = min(min_cnt, cnt)
            continue # 도착하면 조작횟수 갱신만 하고 계속 진행

        # 전진
        di, dj = directions[dir]
        ni, nj = x+di, y+dj
        if 0<=ni<n and 0<=nj<n:
            curr = arr[ni][nj]
            if curr in ('G', 'Y'):
                queue.append((ni, nj, dir, cnt+1, cut))
            # 나무를 만났는데, 나무베기 횟수가 남아있을 경우
            elif curr == 'T' and cut > 0:
                arr[ni][nj] = '.'
                queue.append((ni, nj, dir, cnt+1, cut-1))
                arr[ni][nj] = 'T' #원복

        # 왼쪽 회전
        queue.append((x, y, (dir - 1) % 4, cnt + 1, cut))
        # 오른쪽 회전
        queue.append((x, y, (dir + 1) % 4, cnt + 1, cut))

    return -1  # 도착하지 못할 경우


T = int(input())
for t in range(1, T+1):
    n, k = list(map(int, input().split()))
    arr = [list(input()) for _ in range(n)]
    # print(arr)

    min_cnt = float('inf')
    # 시작 위치 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                start_i, start_j = i, j
    bfs(start_i, start_j, k) # 시작 위치, 남은 나무베기 횟수
    print(f'#{t} {min_cnt}')
