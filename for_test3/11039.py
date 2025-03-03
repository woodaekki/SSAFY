import sys
sys.stdin = open("monster.txt","r")

def bfs(x,y,visited,arr):
    directions = [(0, 1), (0,-1),(1,0),(-1,0)]
    # 시작점 방문 처리 
    cnt = 1
    queue = []
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.pop(0)
        for di,dj in directions:
            ni,nj = x+di,y+dj
            # 1인데 방문 안했으면 처리하고 그 개수 세기
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]==1 and not visited[ni][nj]:
                visited[ni][nj]=1
                queue.append((ni,nj))
                cnt += 1
    return cnt
                        

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            # 1을 발견한 순간 호출 
            if arr[i][j] == 1:
                result = bfs(i,j,visited,arr)
                max_cnt = max(max_cnt, result)
    print(f'#{t} {max_cnt}')