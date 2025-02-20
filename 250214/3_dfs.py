'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v, end): # 현재노드, 종점 노드
    visited = [0] * (end+1) # 문제에서 1번 정점에서 시작하므로
    stack = []  # 스택

    while True:
        if visited[v] == 0:
            visited[v] = 1 # 방문하지 않은 노드 방문 처리
            print(v) # 방문처리한 그 노드 출력
        for w in ad_list[v]:  # 인접 노드 중 방문하지 않았다면 방문 처리
            if visited[w] == 0: 
                stack.append(v)  # 방문한 노드 스택에 push
                v = w  # 방문 처리한 인접 노드가 현재 노드가 됨
                break
        else:  #  더이상 인접 노드 중 방문하지 않은 노드가 없는데
            if stack:  # 스택이 가득차있으면 순서대로 pop
                v = stack.pop()
            else:  # 스택이 비어있으면 종료
                break


n, m, r = map(int, input().split()) # 노드의 수, 간선의 수, 시작정점
graph = list(map(int, input().split()))
ad_list = [[] for _ in range(n+1)]

for i in range(m):
    v1, v2 = graph[i*2], graph[i*2+1] # 노드 연결 정보

    # 양방향
    ad_list[v1].append(v2)
    ad_list[v2].append(v1)

dfs(r,n) # 1번부터 모든 노드를 탐색해라
print(graph)