import sys
sys.stdin = open("graph.txt","r")

def bfs(v, e, adj_lst, start, end, visited):
    directions = [(0,1),(1,0),(1,-1),(1,1)]
    cnt = 0
    # 시작점 방문 
    queue = []
    queue.append((start, cnt))
    visited[start] =1
    
    while queue:
        t, cnt = queue.pop(0)
        # 뺸 노드의 인접 노드가 있는데 방문하지 않았으면면 방문처리
        for w in adj_lst[t]:
            if not visited[w]:
                visited[w]=1
                queue.append((w, cnt+1))
                # 도착하면 최소 카운트 반환
                if w == end:
                    return cnt+1
    return 0 # 못도착하면 0 반환 

T = int(input())
for t in range(1, T+1):
    v, e = list(map(int, input().split()))
    adj_lst = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    for _ in range(e):
        i, j = list(map(int, input().split()))
        adj_lst[i].append(j)
        adj_lst[j].append(i)
    start, end = list(map(int, input().split()))
    result = bfs(v, e, adj_lst, start, end, visited)
    print(f'#{t} {result}')