import sys
sys.stdin = open("bonus.txt","r")

def pang(n,arr):
    maxv = -9999999999
    minv = 999999999999
    for i in range(n):
        for j in range(n):
            sumv = 0
            for k in range(n):
                sumv += arr[i][k]
                sumv += arr[k][j]
            sumv -= arr[i][j]
            if sumv > maxv:
                maxv = sumv
            if sumv < minv:
                minv = sumv
    return maxv - minv

T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = pang(n,arr)
    print(f'#{t} {result}')