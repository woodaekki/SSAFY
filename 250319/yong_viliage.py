import sys
sys.stdin = open("yong.txt", "r")

from collections import deque

def yong_viliage(person):
    queue = deque()
    queue.append(person)
    visited[person] = 1

    # 인접 노드 찾기
    while queue:
        person = queue.popleft()
        for neighbor in graph[person]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = 1

T = int(input())
for t in range(1, T + 1):
    n, m = list(map(int, input().split()))  # 사람 수, 서로 알고 있는 두 사람의 번호 받는 줄 수
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(m):
        i, j = list(map(int, input().split()))
        graph[i].append(j)
        graph[j].append(i)
    # print(graph)
    cnt = 0
    # 방문하지 않았으면, 즉 새로운 무리이면
    for i in range(1, n+1):
        if not visited[i]:
            yong_viliage(i)
            cnt += 1
    print(f'#{t} {cnt}')
