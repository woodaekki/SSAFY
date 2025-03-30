import sys
sys.stdin = open("2.txt", "r")

import heapq
def dijkstra(start):



T = int(input())
for t in range(1, T+1):
    n, e = list(map(int, input().split())) # 노드 수, 간선 수
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        s, e, w = list(map(int, input().split()))
        graph[s].append((e, w))
    result = dijkstra(0)
    print(f'#{t} {result}')

