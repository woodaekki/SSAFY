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
#
# 가로합
column_sums = [0] * m
for i in range(n):
    for j in range(m):
        column_sums[j] += arr[i][j]
print(column_sums)
#
# # 지그재그 출력
# for i in range(n):
#     if i % 2 == 0:
#         # 짝수 번째 행은 왼쪽에서 오른쪽으로 출력
#         for j in range(m):
#             print(arr[i][j], end=" ")
#     else:
#         # 홀수 번째 행은 오른쪽에서 왼쪽으로 출력
#         for j in range(m-1, -1, -1):
#             print(arr[i][j], end=" ")
#     print()  # 한 행 끝나고 줄바꿈
#
# # 123456출력
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j], end = ' ')
# print()
#
# # 누적합
# sumv = 0
# for i in range(n):
#     for j in range(m):
#         sumv += arr[i][j]
#         print(sumv, end = ' ')

# 부분 집합과 그 합
# n = 6
# arr2 = [3, 4, 7, 1, 5, 4]
#
# for i in range(64):  # 2**n
#     sumv = 0
#     for j in range(n):
#         if 1 & (i << j):  # 0이 아닌 수열
#             sumv += arr2[j]
#             print(arr2[j], end=" ")
#     print(sumv)

