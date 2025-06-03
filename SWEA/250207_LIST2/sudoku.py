def sudoku():
    for i in range(9):
        lst = [0]*10
        for j in range(9):
            if lst[arr[i][j]] == 0:
                lst[arr[i][j]] = 1
            else:
                return 0
             
    for j in range(9):
        lst = [0]*10
        for i in range(9):
            if lst[arr[i][j]] == 0:
                lst[arr[i][j]] = 1
            else:
                return 0
 
    # 3x3
    for i in range(0,9,3):
        for j in range(0,9,3):
            lst = [0]*10
            for k in range(3):
                for l in range(3):
                    if 1 <= arr[i+k][j+l] <= 9 and lst[arr[i+k][j+l]] == 0:
                        lst[arr[i+k][j+l]] = 1
                    else:
                        return 0
    return 1                      
             
 
T = int(input())
for t in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = sudoku()
    print(f'#{t} {result}')