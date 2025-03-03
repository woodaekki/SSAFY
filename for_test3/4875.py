import sys
sys.stdin = open("graph.txt","r")

def dfs(x,y, n,arr,visited):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    # 시작점 방문 처리 
    stack = []
    stack.append((x,y))
    visited[x][y]= 1
    
    # 스택에서 빼서 인접한 노드가 1이 아닌데 방문하지 않았으면 방문처리
    while stack:
        x,y = stack.pop(-1)
        for di,dj in directions:
            ni,nj = x+di,y+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj] != '1' and not visited[ni][nj]:
                visited[ni][nj] = 1
                stack.append((ni,nj))
                # 도착점인 3에 도달하면 1 반환 
                if arr[ni][nj] == '3':
                    return 1
    return 0

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    # 시작점은 한개로, 시작점인 2를 찾자바자 dfs호출하기
    found = False
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                result = dfs(i,j, n,arr,visited)
                found = True
                break
        if found:
            break 
    print(f'#{t} {result}')