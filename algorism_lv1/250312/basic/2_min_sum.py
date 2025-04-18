import sys
sys.stdin = open("5.txt", "r")

def recur(row, col):
    if row == n-1 and col == n-1:
        print(path)
        return

    if row+1 < n:
        path.append(arr[row+1][col])
        recur(row+1, col)
        path.pop()
    if col+1 < n:
        path.append(arr[row][col+1])
        recur(row, col+1)
        path.pop()

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    path = [(0, 0, arr[0][0])]
    # result = 10*n*n
    recur(0, 0)
    # print(f'#{t} {result}')