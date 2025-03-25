'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''

def bfs(start, end):  # 시작 정점, 마지막 정점
    visited = [0] * (end+1) # 방문 목록 저장 (정점이 1번부터 시작하므로)
    queue = []
    queue.append(start)
    visited[start] = 1  # 시작점 방문처리
    while queue:        # 큐에 정점이 남아있다면 (front != rear)
        t = queue.pop(0)    # 선입 선출해서
        print(t)
        for w in adj_l[t]:  # 뺀 정점과 인접한 정점 중
            if visited[w] == 0: # 방문하지 않은 정점이 있다면
                queue.append(w)     # 큐에 넣고
                visited[w] = visited[t] + 1 # 방문 처리
    print(visited) # 비상연락망, 전화받은 시간

v, e = map(int, input().split()) # 정점 개수, 간선 개수
graph = list(map(int, input().split()))
# 인접리스트 -------------------------
adj_l = [[] for _ in range(v+1)]
for i in range(e):
    v1, v2 = graph[i*2], graph[i*2+1]
    # 양방향
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

bfs(1, 7) # 1번에서 7번 노드까지 방문하라.
