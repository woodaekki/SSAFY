import sys
sys.stdin = open("2.txt", "r")

def recur(row, total):
    global max_success
    if total <= max_success:
        return

    if row == n:
        max_success = max(max_success, total)
        return

    for person in range(n):
        if not visited[person]:
            visited[person] = True
            recur(row+ 1, total*arr[row][person])
            visited[person] = False


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr[i][j] / 100
    visited = [False] * (n+1)
    max_success = float('-inf')
    recur(0, 1)
    print(f'#{t} {max_success*100:6f}')