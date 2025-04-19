import sys
sys.stdin = open("input.txt", "r")

# 접근법
# - 시작 지점: 전체 다 보아야 한다.
# - 재귀 돌리면서(상하좌우 이동) 숫자를 붙인다
# - 숫자가 7자리가 되면, set에 넣는다. (중복 제거)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def recur(y, x, number):
    if len(number) == 7:    # 7자리가 되면 종료
        result.add(number)
        return

    for i in range(4):  # 상하좌우 확인
        new_y = y + dy[i]
        new_x = x + dx[i]

        # 범위 밖이면 continue
        if new_y < 0 or new_y >= 4 or new_x < 0 or new_x >= 4:
            continue

        # 다음 위치를 추가하면서 진행
        recur(new_y, new_x, number + matrix[new_y][new_x])


T = int(input())
for tc in range(1, T + 1):
    matrix = [input().split() for _ in range(4)]
    result = set()

    for y in range(4):
        for x in range(4):
            recur(y, x, matrix[y][x])

    print(f'#{tc} {len(result)}')
