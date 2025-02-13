import sys
sys.stdin = open("fly3.txt", "r")

def fly3():
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    directions_x = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

    maxplus = maxx = 0
    # + 분사
    for i in range(n):
        for j in range(n):
            sumv = arr[i][j]
            for step in range(1, m):
                for di, dj in directions:
                    ni, nj = i + di*step, j + dj*step
                    if 0 <= ni < n and 0 <= nj < n:
                        sumv += arr[ni][nj]
            if sumv > maxplus:
                maxplus = sumv
            

    # x 분사
    for a in range(n):
        for b in range(n):
            sumv2 = arr[a][b]
            for step2 in range(1, m):
                for di, dj in directions_x:
                    ni, nj = a + di*step2, b+ dj*step2
                    if 0 <= ni < n and 0 <= nj < n:
                        sumv2 += arr[ni][nj]
            if sumv2 > maxx:
                maxx = sumv2
    
    
    if maxplus < maxx:
        return maxx
    else:
        return maxplus

    
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {fly3()}')