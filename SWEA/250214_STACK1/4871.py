def dfs(v,e,adj_lst,visited,i,j,start, end):
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
 
T = int(input())
for t in range(1, T+1):
    v,e = list(map(int, input().split())) #노드수, 몇줄 받을건지
    adj_lst = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    for _ in range(e):
        i, j = list(map(int, input().split()))
        adj_lst[i].append(j)
    start, end = list(map(int, input().split()))
    result = dfs(v,e,adj_lst,visited,i,j,start, end)
    print(f'#{t} {result}')