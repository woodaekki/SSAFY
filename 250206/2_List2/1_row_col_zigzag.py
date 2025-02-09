n,m = 3,4
arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# 세로합
row_sum = [0] * n

for i in range(n):
    for j in range(m):
        row_sum[i] += arr[i][j]
print(row_sum)

# 가로합
column_sums = [0] * m
for i in range(n):
    for j in range(m):
        column_sums[j] += arr[i][j]
print(column_sums)

# 대각선 합
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
s = 0
for i in range(n):
    s += arr[i][i] # 좌측 위에서 우측 아래로 내려가는 대각선
    s += arr[i][n - 1- i] # 우측 위에서 좌측 아래로 내려가는 대각선
s -= arr[5//2][5//2] # 가장 중앙에 있는 값은 2번 더해지므로 차감(행과 열의 크기가 홀수)
print(s)
"""
5
45 15 10 56 23 
96 98 99 40 69 
96 84 49 46 34 
16 64 81 4 11 
10 66 85 55 14 
5
44 91 64 73 62 
78 72 52 73 48 
44 88 55 75 24 
22 72 59 26 62 
87 11 64 79 40 
5
10 10 10 10 10
10 10 10 10 10
10 10 10 10 10
10 10 10 10 10
10 10 10 10 10
"""

# 지그재그 출력
for i in range(n):
    if i % 2 == 0:
        # 짝수 번째 행은 왼쪽에서 오른쪽으로 출력
        for j in range(m):
            print(arr[i][j], end=" ")
    else:
        # 홀수 번째 행은 오른쪽에서 왼쪽으로 출력
        for j in range(m-1, -1, -1):
            print(arr[i][j], end=" ")
    print()  # 한 행 끝나고 줄바꿈

# 123456출력
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
print()

# 누적합
sumv = 0
for i in range(n):
    for j in range(m):
        sumv += arr[i][j]
        print(sumv, end = ' ')



