def omok():
    cnt = 0
    directions = [(0, 1), (1,0), (1,1),(1,-1)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for di,dj in directions:
                    cnt = 1
                    ni,nj= i+di,j+dj
                    while 0<=ni<n and 0<=nj<n and arr[ni][nj]=='o':
                        cnt += 1
                        if cnt == 5:
                            return 'YES'
                        ni += di
                        nj += dj
    return 'NO'
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = omok()
    print(f'#{t} {result}')