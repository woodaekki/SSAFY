import sys
sys.stdin = open("9.txt","r")

def total():
    n, m = list(map(int, input().split()))
    new = [[0]*n for _ in range(m)]
    arr = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new[j][n-1-i] = arr[i][j]
    return new
result = total()
print(result)
