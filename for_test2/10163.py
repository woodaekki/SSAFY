def paper():
    arr = [[0]*1001 for _ in range(1001)]
    n = int(input())
    for k in range(1, n+1):
        a, b, c, d = list(map(int, input().split()))
        for i in range(a, a+c):
            for j in range(b, b+d):
                arr[i][j] = k # 각 색종이 번호로 칠하기 
    
    index = [0]*(n+1)


result = paper()
print(result)