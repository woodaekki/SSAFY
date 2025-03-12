import sys
sys.stdin = open("2.txt", "r")

def space(wall):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)] # 8방향


T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    wall = [[0]*m for _ in range(n)]
    # 4방향 이상 체크할 수 없는 경우 벽 설치
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1:
                wall[i][j] = 1
            if j == 0 or j == m-1:
                wall[i][j] = 1
    result = space(wall)
    print(f'#{t} {result}')