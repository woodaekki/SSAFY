import sys
sys.stdin = open("day.txt", "r")

from collections import deque

def party(person):
    queue = deque()
    queue.append((person, 0))  # (사람 번호, 현재 거리)
    visited[person] = 1
    cnt = 0  # 상원이의 파티에 초대할 친구 수

    while queue:
        current, depth = queue.popleft()

        # 친구의 친구까지만, 즉 depth가 2 이상이면 나옴.
        if depth >= 2:
            continue

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append((neighbor, depth + 1))
                cnt += 1  # 초대할 수 있는 친구 수 증가

    return cnt

T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    result = party(1)
    print(f'#{t} {result}')
