import sys
sys.stdin = open("node.txt", "r")

from collections import deque

def bfs(start, end):
    visited = [0] * (v+1) # 1번부터 출발, 방문 목록 저장

    # 큐 생성 및 시작노드 방문 처리
    queue = deque()
    queue.append(start)
    visited[start] = 1

    # 큐 안에 노드가 남아있을 동안 순회
    while queue:
        # 선입된 노드 빼서 (1번)
        t = queue.popleft()

        # 뺀 노드의 인접노드에서 방문하지 않은 노드가 있다면
        for w in graph[t]:
            if visited[w] == 0:
                visited[w] = visited[t] + 1 # 방문처리 하고 (4, 3번은 거리 1)
                queue.append(w)  # 큐에 넣기
                if w == end: # (1, 4, 3, 6) 즉, 1에서 6번까지 가면
                    return visited[w] - 1 # 출발점 제외 거리 출력

    return 0 # 도착할 수 없으면 0 반환

T = int(input())
for t in range(1,T+1):
    v, e = list(map(int, input().split())) # 노드 수, 간선 수
    graph = [[] for _ in range(v+1)] # 노드 1번부터 시작
    for _ in range(e):
        i, j = list(map(int, input().split())) # i에서 j로 이동
        # 양방향 그래프
        graph[i].append(j)
        graph[j].append(i)

    start, end = list(map(int, input().split()))
    result = bfs(start, end)
    print(f"#{t} {result}")
