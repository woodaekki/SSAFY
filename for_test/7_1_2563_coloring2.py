def color2():
    n = int(input()) # 몇 줄 받을 건지 
    # 빈 리스트 생성
    arr = [[0] * 100 for _ in range(100)]
    for _ in range(n):
        row, col = list(map(int, input().split()))
        for i in range(row, row+ 10):
            for j in range(col, col + 10):
                arr[i][j] = 1
    
    cnt = 0
    for k in range(100):
        for l in range(100):
            if arr[k][l] == 1:
                cnt += 1
    return cnt
            
print(color2())
