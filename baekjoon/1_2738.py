n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    for j in range(m):
        sumv = arr[i][j]
        sumv2 = arr2[i][j]

sumv3 = [[0] * n for _ in range(m)]




