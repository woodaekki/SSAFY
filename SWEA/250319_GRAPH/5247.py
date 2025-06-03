from collections import deque
 
def bfs(n, cnt):
    queue = deque()
    queue.append((n, 0)) # 시작 숫자, 연산 횟수
    visited = set([(n)])
 
    while queue:
        curr, cnt = queue.popleft()
        operators = [curr+1, curr-1, curr*2, curr-10]
        if curr == m:
            return cnt
        for cal in operators:
            if 0 <= curr <= 1000000 and cal not in visited:
                visited.add(cal)
                queue.append((cal, cnt+1))
 
 
T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    result = bfs(n, 0)
    print(f'#{t} {result}')