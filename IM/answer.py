import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    n = int(input())  # 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(n)]  # 배열 입력

    # 상, 하, 좌, 우 이동 방향 (4방향)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    maxi = 0  # 최대 길이 저장

    # 모든 시작점을 순회
    for i in range(n):
        for j in range(n):
            cnt = 1  # 시작점에서 시작하므로 길이는 최소 1
            r, c = i, j  # 현재 위치
            while True:
                mini = arr[r][c]  # 최소값을 초기화 (현재 위치)
                next_r, next_c = -1, -1  # 다음 이동할 위치
                for k in range(4):  # 4방향 탐색
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] < mini:  # 범위 안에 있고, 더 작은 값이면
                        mini = arr[nr][nc]
                        next_r, next_c = nr, nc  # 새로운 위치로 이동
                if next_r == -1:  # 더 이상 이동할 곳이 없으면
                    break
                r, c = next_r, next_c  # 새로운 위치로 갱신
                cnt += 1  # 길이 증가

            # 최대 길이 갱신
            maxi = max(maxi, cnt)

    # 테스트 케이스마다 결과 출력
    print(f"#{test_case} {maxi}")
