# import sys
# from pprint import pprint as print
# sys.stdin = open("bfs2.txt", "r")

def dfs(x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    for di, dj in directions:
        ni, nj = x+di, y+dj
        while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 1:
            visited[ni][nj] = 1
            ni += di
            nj += dj
    
    # 안전한 칸 개수 세기
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0 and not visited[i][j]:
                cnt += 1
    return cnt

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    
    # 괴물 위치 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                monster = dfs(i, j)
    print(f"#{t} {monster}")
