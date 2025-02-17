# import sys
# sys.stdin = open("algo2_sample_in.txt", "r")

def rgb():
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # R괴물 (1칸)
    for i in range(10):
        for j in range(10):
            sumv = arr[i][j]
            for di, dj in directions:
                for step in range(1, arr[i][j]+1):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        sumv += arr[ni][nj]

    # G괴물(2칸)
    for i in range(10):
        for j in range(10):
            sumv = arr[i][j]
            for di, dj in directions:
                for step in range(1, 2):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        sumv += arr[ni][nj]

    # B괴물(3칸)
    for i in range(10):
        for j in range(10):
            sumv = arr[i][j]
            for di, dj in directions:
                for step in range(1, 3):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        sumv += arr[ni][nj]
    return sumv

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(10)]
    result = rgb()
    print(f'#{t} {result}')