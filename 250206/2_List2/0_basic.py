# """
# 0 0 0
# 0 0 0
# 0 0 0
# """
# # arr = [[0] * 3 for _ in range(3)]
# # print(arr)

# """
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# """
# # 1. 배열 행과 열의 크기가 같을 때
# # n = int(input()) # 배열 행과 열의 크기
# # arr = [list(map(int, input().split())) for _ in range(n)]
# #
# # for i in range(n):
# #     for j in range(n):
# #         print(arr[i][j])

# """
# 3 4
# 1 2 3 4
# 4 5 6 5
# 7 8 9 10
# """
# # 2. 배열 행과 열의 크기가 다를 때, 저장된 값의 누적합 출력하기
# # n, m = map(int, input().split())
# # arr = [list(map(int, input().split())) for _ in range(n)]
# #

# # arr = []
# # for _ in range(n):
# #     arr.append(list(map(int, input().split())))

# # s = 0
# # for i in range(n):
# #     for j in range(m):
# #         s += arr[i][j]
# #         print(s)

# """
# 3 4
# 1 2 3 4 -> 10
# 5 6 7 8 -> 26
# 7 8 9 10 -> 34
# """
# # 3. 가로 열 한줄마다의 합 구하기
# # n, m = map(int, input().split())
# # arr = [list(map(int, input().split())) for _ in range(n)]
# #
# # s = 0
# # for i in range(n):
# #     for j in range(m):
# #         s += arr[i][j]
# #         print(s)

# # 4. 지그재그 순회
# # n, m = map(int, input().split())
# # arr = [list(map(int, input().split())) for _ in range(n)]
# #
# # for i in range(n): # i를 고정시켜놓고
# #     for j in range(m):
# #         if: # 짝수일때 오른쪽으로
# #         else: # 홀수일때 왼쪽으로
# #             print(zigzag)

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




