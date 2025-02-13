def list2():
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr2 = [list(map(int, input().split())) for _ in range(n)]

    sumv = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            sumv[i][j] = arr[i][j] + arr2[i][j]
    return sumv

result = list2()
for ans in result:
    print(*ans)

