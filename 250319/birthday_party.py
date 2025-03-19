import sys
sys.stdin = open("day.txt", "r")

from collections import deque

def party(person, cnt):
    queue = deque()
    queue.append((person, 0))
    visited[person] = 1
    
    # 상원의 친한 친구 수 구하기
    while queue:
        person, cnt = queue.popleft()
        for neighbor in graph[person]:
            if not visited[neighbor]:
                queue.append((neighbor, cnt+1))
                visited[neighbor] = 1
    return cnt

T = int(input())
for t in range(1, T + 1):
    n, m = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(m):
        i, j = list(map(int, input().split()))
        graph[i].append(j)
        graph[j].append(i)
    # print(graph)
    result = party(1, 0)
    print(f'#{t} {result}')