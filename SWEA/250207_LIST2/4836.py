def paper():
    arr = [[0]*10 for _ in range(10)]
    n = int(input())
    for _ in range(n):
        a,b,c,d,color = list(map(int, input().split()))
        for i in range(a,c+1):
            for j in range(b,d+1):
                arr[i][j] += color
     
    cnt = 0
    for m in range(10):
        for l in range(10):
            if arr[m][l] == 3:
                cnt += 1
    return cnt   
 
T = int(input())
for t in range(1,T+1):
    result = paper()
    print(f'#{t} {result}')