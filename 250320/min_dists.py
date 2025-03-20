import sys
sys.stdin = open("dists.txt", "r")


import heapq
# 단방향
def dijkstra(start):
    heap_queue = []  # (누적 거리, 노드 번호)
    heapq.heappush(heap_queue, (0, start))  # (거리, 노드)
    min_dists = [float("inf")] * (N + 1)  # 노드 번호가 0~N까지이므로 N+1 크기
    min_dists[start] = 0

    while heap_queue:
        weight, node = heapq.heappop(heap_queue)  # 거리 우선으로 pop

        if min_dists[node] < weight:
            continue

        for next_node, next_weight in graph[node]:
            new_weight = weight + next_weight

            if min_dists[next_node] > new_weight:
                min_dists[next_node] = new_weight
                heapq.heappush(heap_queue, (new_weight, next_node))  # 거리 우선 정렬

    return min_dists


T = int(input())

for t in range(1, T + 1):
    N, E = map(int, input().split())  # 마지막 노드 번호, 간선 개수
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    # 0번 정점에서 모든 노드까지 최단 거리 계산
    result = dijkstra(0)
    print(f"#{t} {result[N]}")