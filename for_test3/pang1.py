import sys
sys.stdin = open("pang.txt","r")

def pang(n,m,arr):
    maxv = -9999999999
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    for i in range(n):
        for j in range(m):
            sumv = arr[i][j]
            for step in range(1, arr[i][j]+1):
                for di,dj in directions:
                    ni,nj = i+di*step,j+dj*step
                    if 0<=ni<n and 0<=nj<m:
                        sumv += arr[ni][nj]
                if sumv > maxv:
                    maxv = sumv
    return maxv

T = int(input())
for t in range(1,T+1):
    n,m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = pang(n,m,arr)
    print(f'#{t} {result}')