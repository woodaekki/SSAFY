def bfs(x,y,n,arr,visited):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    cnt = 0
    # 시작점 방문 
    queue = []
    queue.append((x,y,cnt))
    visited[x][y] =1
 
    while queue:
        x,y,cnt = queue.pop(0)
        # 방문하지 않은 인접이 1이 아니면 방문처리 
        for di,dj in directions:
            ni,nj = x+di,y+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj] != '1' and not visited[ni][nj]:
                queue.append((ni,nj,cnt+1))
                visited[ni][nj] = 1
                # 도착지에 도착하면 최소칸수 반환
                if arr[ni][nj] == '3':
                    return cnt
    return 0 # 경로가 없는 경우 
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
 
    # 출발지인 2지점을 찾으면 멈추고 bfs 호출
    found = False
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                result = bfs(i,j,n,arr,visited)
                found = True
                break
        if found:
            break
    print(f'#{t} {result}')