T = int(input())

def snail():
    n = int(input())  # n * n
    arr = [[0] * n for _ in range(n)]  # 빈 배열 생성

    # 우, 하, 좌, 상 순서로
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0  # 처음에는 오른쪽 방향으로 시작
    row, col = 0, 0  # 시작 위치는 (0, 0)

    for i in range(1, n * n + 1):  # 1부터 n*n까지 채움
        arr[row][col] = i  # 현재 칸에 값 채우기
        newr = row + directions[d][0]  # 새로운 행
        newc = col + directions[d][1]  # 새로운 열

        # 새로운 위치가 배열의 범위를 벗어나거나 이미 채워져 있으면 방향 전환
        if newr < 0 or newr >= n or newc < 0 or newc >= n or arr[newr][newc] != 0:
            d = (d + 1) % 4  # 방향을 시계방향으로 전환
        row += directions[d][0]
        col += directions[d][1]
    return n, arr # 튜플로 받았으니

for t in range(1, T + 1):
    result = snail()
    print(f'#{t}')
    for row in range(result[0]): # result[0] = n
        print(*result[1][row]) # result[1] = arr