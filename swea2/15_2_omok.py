import sys

sys.stdin = open("omok.txt", "r")


def omok():
    n = int(input())  # n x n 배열 크기
    arr = [list(input().strip()) for _ in range(n)]  # 배열 입력 받기

    # 오목을 체크할 방향 (가로, 세로, 두 대각선)
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # (dy, dx)로 방향을 설정

    # 오목 체크 함수
    def check_win(y, x, dy, dx):
        count = 0
        for i in range(5):  # 오목이 5개 연속으로 되어 있는지 확인
            ny, nx = y + i * dy, x + i * dx
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 'o':
                count += 1
            else:
                break
        return count == 5  # 5개 연속된 'o'가 있으면 True

    # 보드 탐색
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':  # 'o'를 발견했을 때
                # 네 방향 (가로, 세로, 두 대각선)에 대해 오목 체크
                for dy, dx in directions:
                    if check_win(i, j, dy, dx):
                        return "YES"

    return "NO"  # 오목이 없으면 "NO"


T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    print(f'#{t} {omok()}')
