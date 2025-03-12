import sys
sys.stdin = open("7.txt", "r")
# def change(k):
#     if k == change_cnt:
#         ...
#         return
#
#     for i in range(n-1):
#         for j in range(i+1, n):
#             #데이터 교환
#             change(k+1, #데이터 교환)
#             # 원복

# 백트래킹: 같은 깊이의 같은 수가 나오면 가지를 치자.

T = int(input())
for t in range(1, T+1):
    arr, change = map(int, input().split())
    new_arr = list(arr)
    print(new_arr)