# import sys
# sys.stdin = open("1.txt", "r")

# .: 비어있는 곳/ #:벽 / S:현재 위치/ E: 문의 위치/ X: 챙겨야할 물건 (최대 5개)
# 1

# 최소 이동 시간
# S -> E

n, m = list(map(int, input().split()))
arr = [list(input()) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        # 챙길 물건의 개수 세기
        if arr[i][j] == 'X':
            cnt += 1
print(cnt)


print(arr)