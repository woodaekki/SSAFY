import sys
sys.stdin = open("1.txt", "r")

def recur(row, col, total):
    global min_total
    if total > min_total:
        return

    if row == n-1 and col == n-1:
        min_total = min(min_total, total+arr[row][col])
        return

    # 오른쪽
    if col+1 < n:
        recur(row, col+1, total+arr[row][col])
    # 아래
    if row+1 < n:
        recur(row+1, col, total+arr[row][col])

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_total = float('inf')
    recur(0, 0, 0)
    print(f'#{t} {min_total}')