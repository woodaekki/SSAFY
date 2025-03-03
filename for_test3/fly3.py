import sys
sys.stdin = open("in1.txt","r")

def pang(n,m,arr):
    maxv = -9999999999
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    # 가로열
    for i in range(n):
        for j in range(n):
            sumv = arr[i][j]
            for step in range(1,m):
                for di,dj in directions:
                    ni,nj = i+di*step,j+dj*step
                    if 0<=ni<n and 0<=nj<n:
                        sumv += arr[ni][nj]
                if sumv > maxv:
                    maxv = sumv
    
    maxv2 = -99999999999
    directions2 = [(1,1),(1,-1),(-1,-1),(-1,1)]
    # 대각선열
    for i in range(n):
        for j in range(n):
            sumv2 = arr[i][j]
            for step2 in range(1,m):
                for di,dj in directions2:
                    ni,nj = i+di*step2,j+dj*step2
                    if 0<=ni<n and 0<=nj<n:
                        sumv2 += arr[ni][nj]
                if sumv2 > maxv2:
                    maxv2 = sumv2
    
    if maxv > maxv2:
        return maxv
    else:
        return maxv2

T = int(input())
for t in range(1,T+1):
    n,m = list(map(int, input().split())) # nxn배열, m의 세기 
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = pang(n,m,arr)
    print(f'#{t} {result}')
