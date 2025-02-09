# 상하좌우 k칸의 합계 중 최댓값 구하기
# 최댓값의 중앙값 인덱스 구하기 
n, m, k = 5, 5, 2
arr = [
   [1, 1, 1, 1, 1],
   [1, 2, 3, 4, 5],
   [1, 2, 3, 4, 5], 
   [1, 2, 3, 4, 5],
   [1, 1, 1, 1, 1]
]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
maxv = 0
max_i = 0
max_j = 0

for i in range(n):
   for j in range(m):
       sumv = arr[i][j]
       for di, dj in directions:
           for step in range(1, k + 1):
               ni, nj = i + di * step, j + dj * step
               if 0 <= ni < n and 0 <= nj < m:
                   sumv += arr[ni][nj]
       if sumv > maxv:
           maxv = sumv
           max_i = i  # 인덱스 저장
           max_j = j  # 인덱스 저장

print(f"최대값: {maxv}")
print(f"인덱스: ({max_i}, {max_j})") 
