import sys
sys.stdin = open("1012.txt", "r")

def cabbage():
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    stack = []
    stack.append((i, j))
    visited[i][j] = True

    while stack:
        t = stack.pop(-1)

        for di, dj in directions:
            ni, nj = i+di, j+dj
            # 범위 벗어나지 않았고, 배추가 있는데, 방문하지 않았으면
            if 0 <= ni < n and 0 <= nj < m and arr[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True # 방문 처리하고
                stack.append((i, j)) # 스택에 넣기


T = int(input())
for t in range(1, T+1):
    m, n, k = list(map(int, input().split())) # 가로, 세로, 배추 총 개수
    arr = [[0] * m for _ in range(n)]
    visited = [[False]*m for _ in range(n)] # 방문 목록 저장

    for _ in range(k):
        j, i = list(map(int, input().split())) # 배추가 저장된 가로 세로 좌표
        arr[i][j] = 1 # 배추 위치 저장


result = cabbage()
print(result)