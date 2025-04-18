import sys
sys.stdin = open("2.txt", "r")

def space():
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)] # 8방향
    spot = 0 # 예비 후보지 개수

    for i in range(n):
        for j in range(m):
            cnt = 0 # 낮은지역이 총 4곳인지 체크하기 위한 변수
            # 낮은 후보지
            low = arr[i][j]
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    if arr[ni][nj] < low:
                        cnt += 1
            if cnt >= 4:
                spot += 1
    return spot

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = space()
    print(f'#{t} {result}')