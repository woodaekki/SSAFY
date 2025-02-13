def forcaster(h, w, arr):
    new_arr = [[-1] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'c':
                new_arr[i][j] = 0
                k = j+1
                while k < w and arr[i][k] == '.':
                    new_arr[i][k] = new_arr[i][k-1] + 1
                    k += 1
    return new_arr         

h, w = map(int, input().split())
arr = [list(map(str, input())) for _ in range(h)]
result = forcaster(h, w, arr)
for ans in result:
    print(*ans)