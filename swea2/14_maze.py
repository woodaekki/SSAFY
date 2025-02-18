import sys
sys.stdin = open("maze.txt", "r")

def dfs(stR, stC):
    stack = []
    visited = [[False] * n for _ in range(n)]

    stack.append((stR, stC))
    visited[stR][stC] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while stack:
        curR, curC = stack.pop()
        for dr, dc in directions:
            newR = curR + dr
            newC = curC + dc
            # 범위 내에 있는데 방문하지 않았으면
            if 0 <= newR < n and 0 <= newC < n and not visited[newR][newC]:
                # 구멍이면 방문처리하고, 스택에 넣기
               if arr[newR][newC] == 0:
                   stack.append((newR, newC))
                   visited[newR][newC] = True
                # 도착하면 1 반환
               elif arr[newR][newC] == 3:
                   return 1
    return 0

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    # 출발지인 2 찾기
    for i in range(n):
        if arr[i].count(2): # 2가 하나밖에 없으니까
            j = arr[i].index(2) # 만약 2가 없을시에 에러발생 위험 방지 !
            break
    print(f'#{t} {dfs(i, j)}')