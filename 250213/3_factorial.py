# 필요한 함수가 자신과 같은 경우 자신을 다시 호출하는 구조

# 모든 배열의 원소에 접근해 보는 방식
# def f(i, N): # 배열의 인덱스, 배열의 길이값
#     if i==N:    # 중단조건
#         return
#     else:  # 재귀호출
#         print(arr[i])
#         f(i+1, N)
#
# arr = [1, 2, 3]
# f(0, 3)
#
# # 배열에 v가 있으면 1, 없으면 0을 리턴
# def f(i, N, V):  # 배열의 인덱스, 배열의 길이값, 찾는값
#     if i == N:
#         return 0
#     elif A[i] == V:  # 찾은 경우
#         return 1
#     else:  # 재귀호출
#         return f(i + 1, N, V)
#
# N = 3
# A = [3, 7, 6]
# V = 6
# ans = f(0, N, V)
# print(ans)

# 피보나치
def fibo(n):
    if n < 2:
        return n
    else:
        f1 = fibo(n-1)
        f2 = fibo(n-2)
    return f1 + f2

fibo(5)

