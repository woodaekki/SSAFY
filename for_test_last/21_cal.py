import sys
sys.stdin = open("1.txt", "r")

from collections import deque

def bfs(curr, cnt):
    # 시작점 방문
    queue = deque()
    queue.append((n, 0))
    visited = set([(n)])

    while queue:
        curr, cnt = queue.popleft()
        if curr == m:
            return cnt
        operator = [curr+1, curr-1, curr*2, curr-10]
        for cal in operator:
            if 1 <= cal <= 1000000 and cal not in visited:
                queue.append((cal, cnt+1))
                visited.add(cal)

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split())) # 원본, 만들려는 수
    result = bfs(n, 0)
    print(f'#{t} {result}')

