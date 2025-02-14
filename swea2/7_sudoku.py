import sys
sys.stdin = open("sudo.txt", 'r')

def sudoku():
    # 가로방향 체크
    for i in range(9):
        sudoku1 = [0] * 10
        for j in range(9):
            num = arr[i][j]
            if sudoku1[num] == 1:
                return 0
            sudoku1[num] = 1

    # 세로방향 체크
    for j in range(9):
        sudoku2 = [0] * 10
        for i in range(9):
            num2 = arr[i][j]
            if sudoku2[num2] == 1:
                return 0
            sudoku2[num2] = 1
    # 3 * 3배열 체크
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sudoku3 = [0] * 10
            for x in range(3):
                for y in range(3):
                    num3 = arr[i+x][i+y]
                    if sudoku3[num3] == 1:
                        return 0
                    sudoku3[num3] = 1
                    # print(i + x, j + y)
    return 1

T = int(input())
for t in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    print(f'#{t} {sudoku()}')