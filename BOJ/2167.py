def maze():
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    visited = [[False] * m for _ in range(n)] # 방문 리스트 저장 
    visited[0][0] = True

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    count = 0

    # 1은 구멍 / 0은 벽
    for i in range(n):
        for j in range(m):
            curr = arr[1][1]
            # 인접한 상하좌우 1칸씩 들여다봤을때
            for di, dj in directions:
                ni, nj = i+di, j+dj
                # 그래프 범위 안에 있는데, 구멍이고 방문하지 않았다면 
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == False:
                    visited[ni][nj] = True # 방문처리 하고
                    cnt += 1 # 카운트 1증가 
                elif arr[ni][nj] == 0:
                    break
    return cnt 


print(maze())