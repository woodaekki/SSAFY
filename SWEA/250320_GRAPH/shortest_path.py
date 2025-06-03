import heapq
 
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # 가중치, 노드
 
    dist = [float('inf')] * (N+1)
    dist[start] = 0
 
    while queue:
        weight, node = heapq.heappop(queue)
        for next_weight, next_node in graph[node]:
            new_weight = weight + next_weight
            if new_weight < dist[next_node]:
                dist[next_node] = new_weight
                heapq.heappush(queue, (new_weight, next_node))
 
    return dist[N]
 
T = int(input())
for t in range(1, T+1):
    N, E = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = list(map(int, input().split()))
        graph[s].append((w, e))
    result = dijkstra(0)
    print(f'#{t} {result}')