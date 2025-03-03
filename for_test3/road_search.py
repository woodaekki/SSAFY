import sys
sys.stdin = open("graph.txt","r")

def dfs(tc,n,graph,adj_lst,visited, start, end):
    # 시작점 방문 처리 
    stack = []
    stack.append(start)
    visited[start]= 1
    
    # 시작점의 인접 노드가 있는데 방문하지 않았으면 방문처리
    while stack:
        t = stack.pop(-1)
        for w in adj_lst[t]:
            if not visited[w]:
                visited[w]=1
                stack.append(w)
                # 계속 빼다가, 그 뺸 노드가 마지막 노드가 되면 도착한것, 1반환
                if w == end:
                    return 1
    return 0

T = 10
for t in range(1, T+1):
    tc, n = list(map(int, input().split())) #테케, 노드수 
    graph = list(map(int, input().split()))
    adj_lst = [[] for _ in range(n)]
    visited = [0]*100
    start, end = 0, 99
    for i in range(n):
        adj_lst[graph[i*2]].append(graph[i*2+1])

    result = dfs(tc,n,graph,adj_lst,visited, start, end)
    print(f'#{t} {result}')