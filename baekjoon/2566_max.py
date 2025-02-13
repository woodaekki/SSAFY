def list2():
    arr = [list(map(int, input().split())) for _ in range(9)]

    max_arr = -1
    for i in range(9):
        for j in range(9):
            if arr[i][j] >= max_arr:
                max_arr = arr[i][j]
                row = j + 1
                col = i + 1
    return max_arr, col, row

result = list2()
print(result[0])
print(result[1], result[2])