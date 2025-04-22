import sys
sys.stdin = open("1.txt", "r")

def solve(n):
    arr = [[0] * n for _ in range(n)]  # n x n 배열 생성
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래쪽, 왼쪽, 위쪽
    row, col, dir_idx = 0, 0, 0  # 시작점과 방향 인덱스
    num = 1

    for _ in range(n * n):
        arr[row][col] = num  # 현재 위치에 숫자 채우기
        num += 1

        # 다음 위치 계산
        next_row, next_col = row + directions[dir_idx][0], col + directions[dir_idx][1]

        # 경계를 벗어나지 않으며, 아직 방문하지 않은 칸이라면
        if 0 <= next_row < n and 0 <= next_col < n and arr[next_row][next_col] == 0:
            row, col = next_row, next_col  # 유효한 위치로 이동
        else:
            # 방향 변경 (시계방향)
            dir_idx = (dir_idx + 1) % 4
            row, col = row + directions[dir_idx][0], col + directions[dir_idx][1]

    return result

T = int(input())
for t in range(1, T + 1):
    n = int(input())  # 각 테스트 케이스마다 n 값 입력
    result = solve(n)
    print(f'#{t}', **result)

