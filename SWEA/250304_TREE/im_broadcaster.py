def solve():
    visited = [[0]*n for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(n):
        for j in range(n):
            light = arr[i][j]
            # a,b,c일때 전파가 닿는 범위
            if light == 'A' or light == 'B' or light == 'C':
                if light == 'A':
                    m = 1
                if light == 'B':
                    m = 2
                if light == 'C':
                    m = 3
 
                for di,dj in directions:
                    for step in range(1, m+1):
                        ni,nj = i+di*step, j+dj*step
                        if 0<=ni<n and 0<=nj<n:
                            # 전파가 닿는 곳 방문처리하기
                            visited[ni][nj] = 1
 
    cnt = 0
    for m in range(n):
        for l in range(n):
            # 'H' 표시된 곳중 방문처리 안된 곳만 카운트 증가
            if arr[m][l] == 'H' and not visited[m][l]:
                cnt += 1
    return cnt
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = solve()
    print(f'#{t} {result}')