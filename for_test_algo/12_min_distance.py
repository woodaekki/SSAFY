import sys
sys.stdin = open("2.txt", "r")

import heapq
def dijkstra(start):
    # 시작점 방문


T = int(input())
for t in range(1, T+1):
    n, e = list(map(int, input().split())) # 노드 수, 간선 수

    result = dijkstra(0)

