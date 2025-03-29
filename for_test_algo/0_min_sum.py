# import sys
# sys.stdin = open("2.txt", "r")

def recur(row, col, total):
    global min_sum
    if row == n-1 and col == n-1:
        min_sum = min(min_sum, total+arr[row][col])
        return

    # 오른쪽
    if col < n-1:
        recur(row, col+1, total+arr[row][col])
    # 아래쪽
    if row < n-1:
        recur(row+1, col, total+arr[row][col])


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = float('inf')
    recur(0, 0, 0)
    print(f'#{t} {min_sum}')
