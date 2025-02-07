# 5. 4방향의 인접 요소를 탐색하기
n, m = 2, 3
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(n):
    for j in range(m):
        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m:
                print(ni, nj)

# 6. 상하좌우 k칸의 합계 중 최댓값

# 7. 전치 행렬
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# 8. i,j의 크키에 따라 접근하는 원소 비교 (교재 참고)

