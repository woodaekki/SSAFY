def long(node, cnt):
    global max_cnt
    # print(visited, cnt)
    max_cnt = max(max_cnt, cnt)
    visited[node] = 1
    # 인접했는데 방문하지 않았으면 재귀
    for w in graph[node]:
        if not visited[w]:
            long(w, cnt+1)
    visited[node] = 0
 
T = int(input())
for t in range(1, T + 1):
    n, m = list(map(int, input().split()))  # 정점 수, 간선 수
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(m):
        i, j = list(map(int, input().split()))
        graph[i].append(j)
        graph[j].append(i)
    # print(graph)
    max_cnt = -1
    for i in range(1, n+1):
        if not visited[i]:
            long(i, 1)
    print(f'#{t} {max_cnt}')