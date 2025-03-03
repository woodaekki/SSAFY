import sys
sys.stdin = open("graph.txt","r")

def dfs(n,arr):
    directions = [(0,1),(1,0),(1,-1),(1,1)]
    for i in range(n):
        for j in range(n):
            # 오목돌을 발견한 순간 우,하,대각선으로 확인하기 
            if arr[i][j] == 'o':
                for di,dj in directions:
                    cnt = 1
                    ni,nj = i+di,j+dj
                    while 0<=ni<n and 0<=nj<n and arr[ni][nj] == 'o':
                        cnt += 1
                        # 돌이 5개가 되는게 있으면 'YES'반환
                        if cnt == 5:
                            return 'YES'
                        ni += di
                        nj += dj   
    return 'NO'

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = dfs(n,arr)
    print(f'#{t} {result}')