def bonus():
    n = int(input()) # n x n
    arr = [list(map(int, input().split())) for _ in range(n)]  # n줄
    maxv, minv = 0, 999999
 
    for i in range(n):
        for j in range(n):
            sumv = 0
            for k in range(n):
                sumv += arr[i][k] # 가로합
                sumv += arr[k][j] # 세로합
            sumv -= arr[i][j]
            if maxv < sumv:
                maxv = sumv
            if minv > sumv:
                minv = sumv
    return maxv - minv
 
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {bonus()}')