def bfs(start, end, adj_lst, v):
    queue = []
    cnt = 0
    queue.append((start, cnt)) # 시작 노드, 최소 칸수 
    visited[start] = 1
     
    while queue:
        t, cnt = queue.pop(0)
        for w in adj_lst[t]:
            if not visited[w]:
                visited[w]=1
                queue.append((w, cnt+1))
                if w == end:
                    return cnt+1
    return 0
 
T = int(input())
for t in range(1, T + 1):
    v, e = list(map(int, input().split())) # 노드수, 몇줄받을건지 
    adj_lst = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    for _ in range(e):
        i,j = list(map(int, input().split()))
        adj_lst[i].append(j)
        adj_lst[j].append(i)
    start, end = list(map(int, input().split()))
    print(f'#{t} {bfs(start, end, adj_lst, v)}')