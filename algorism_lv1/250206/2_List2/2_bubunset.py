# 부분집합의 합 문제 구현하기
n = 5
arr = [[1,2,3,4,5],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]
sum = 0

for row in range(n):
    for col in range(n):
        sumv = 0

        # 상단의 좌표
        newr = row - 1
        # print(newr)
        newc = col
        # print(newc)
        # print(arr[newr][newc])
        if 0 <= newr < n and 0 <= newc < n:
            sumv += arr[newr][newc] - arr[row][col]

        # 하단의 좌표
        newr = row + 1
        newc = col
        if 0 <= newr < n and 0 <= newc < n:
            sumv += arr[newc][newr] - arr[col][row]