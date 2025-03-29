import sys
sys.stdin = open("2.txt", "r")

from collections import deque

def bfs(n, cnt):
    # 시작점 방문
    queue = deque()
    queue.append((n,cnt))
    visited = set([n])

    while queue:
        curr, cnt = queue.popleft()
        operators = [curr+1, curr-1, curr*2, curr-10]
        if curr == m:
            return cnt
        for cal in operators:
            if 1 <= cal <= 1000000 and cal not in visited:
                queue.append((cal, cnt+1))
                visited.add(cal)

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    result = bfs(n, 0)
    print(f'#{t} {result}')