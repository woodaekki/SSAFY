import sys
sys.stdin = open("1.txt", "r")

def solve():
    arr = [[0] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    row, col, dir_idx = 0, 0, 0
    num = 1

    for _ in range(n * n):
        arr[row][col] = num
        num += 1

        next_row, next_col = row + directions[dir_idx][0], col + directions[dir_idx][1]
        if 0 <= next_row < n and 0 <= next_col < n and arr[next_row][next_col] == 0:
            row, col = next_row, next_col
        else:
            # 방향 변경
            dir_idx = (dir_idx + 1) % 4
            row, col = row + directions[dir_idx][0], col + directions[dir_idx][1]
    return arr

T = int(input())
for t in range(1, T+1):
    n = int(input())
    result = solve()
    print(f'#{t} {result}')
