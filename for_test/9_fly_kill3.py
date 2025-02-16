def fly3():
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    directions_x = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

    # + 분사
    maxplus = -9999999999999999
    for i in range(n):
        for j in range(n):
            sumv = arr[i][j]
            for di, dj in directions:
                for step in range(1,m):
                    ni, nj = i+di*step, j+dj*step 
                    if 0 <= ni < n and 0 <= nj < n:
                        sumv += arr[ni][nj]
            if sumv > maxplus:
                maxplus = sumv
    
    # x 분사
    maxx = -9999999999999999
    for i in range(n):
        for j in range(n):
            sumv2 = arr[i][j]
            for di, dj in directions_x:
                for step in range(1,m):
                    ni, nj = i+di*step, j+dj*step 
                    if 0 <= ni < n and 0 <= nj < n:
                        sumv2 += arr[ni][nj]
            if sumv2 > maxx:
                maxx = sumv2
    
    if maxx > maxplus:
        return maxx
    else:
        return maxplus

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {fly3()}')
    
 
    
 
     
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {fly3()}')