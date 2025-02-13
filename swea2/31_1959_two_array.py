import sys
sys.stdin = open("two.txt", "r")

# 길이가 3, 5면
# 길이가 5인 배열의 앞의 3개와의 곱
# 또는 뒤의 3개와의 곱의 합 중
# 큰 합을 반환 

def two():
    a, b = map(int, input().split())  # arr_a와 arr_b의 길이
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    if len(arr_a) > len(arr_b):
        a, b = b, a

    # i = 0일때,
    # arr_a[0]과 arr_b[0+0] 곱함
    # arr_a[1]과 arr_b[0+1] 곱함

    # i = 1일때,
    # arr_a[0]과 arr_b[1+0] 곱함
    # arr_a[1]과 arr_b[1+1] 곱함

    for i in range(b-a+1):
        sumv = 0
        for j in range(len(arr_a)):
            sumv += arr_a[j] * b[i+j]
        maxv = max(maxv, sumv)
    return maxv


T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    print(f'#{t} {two()}')

