def solve():
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래쪽, 왼쪽, 위쪽
    new_arr = []  # 결과 배열
    row, col, dir_idx = 0, 0, 0  # 시작점과 방향 인덱스

    for _ in range(n * n):
        new_arr.append(arr[row][col])

        # 다음 위치 계산
        next_row, next_col = row + directions[dir_idx][0], col + directions[dir_idx][1]

        if 0 <= next_row < n and 0 <= next_col < n:
            row, col = next_row, next_col
        else:
            dir_idx = (dir_idx + 1) % 4
            row, col = row + directions[dir_idx][0], col + directions[dir_idx][1]

    return new_arr

# 실행
result = solve()
print(result)
