import sys
sys.stdin = open("fly.txt", "r")

def fly():
    n,m = list(map(int, input().split())) # n x n 배열, m x m 파리채
    arr = [list(map(int, input().split())) for _ in range(n)]
     
    max_fly = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0 # 죽인 파리의 합
            for k in range(i, i+m):
                for l in range(j, j+m):
                    cnt += arr[k][l]
                    if cnt > max_fly:
                        max_fly = cnt
    return max_fly
    
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {fly()}')