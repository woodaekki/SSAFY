import sys
sys.stdin = open("graph.txt","r")

def bfs(x,y,n,arr,visited):
    cnt = 1
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    # 시작점 방문 
    queue = []
    queue.append((x,y))
    visited[x][y] =1

    while queue:
        x,y = queue.pop(0)
        # 방문하지 않은 인접이 1이 아니면 방문처리 
        for di,dj in directions:
            ni,nj = x+di,y+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj] == '1' and not visited[ni][nj]:
                queue.append((ni,nj))
                visited[ni][nj]=1
                cnt += 1
    return cnt


n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
area = 0
result = []
for i in range(n):
    for j in range(n):
        # 1 발견하는 순간 호출 
        if arr[i][j] == '1' and not visited[i][j]:
            area += 1 # 호출할때마다 구역 카운트 증가 
            result.append(bfs(i,j,n,arr,visited))

print(area)
sorted_result = sorted(result)
for re in sorted_result:
    print(re)

    