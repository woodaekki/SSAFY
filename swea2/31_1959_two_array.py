import sys
sys.stdin = open("two.txt", "r")

# 길이가 3, 5면
# 길이가 5인 배열의 앞의 3개와의 곱
# 또는 뒤의 3개와의 곱의 합 중
# 큰 합을 반환 

def two():
    a, b = list(map(int, input().split()))  # arr_a와 arr_b의 길이
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    max_sum = -9999999999 

    # for i in range(abs(a - b) + 1):  
    #     sumv = 0  
    #     for j in range(min(a, b)):  
    #         if 0 <= i + j < b and 0 <= j < a:
    #             sumv += arr_a[j] * arr_b[i + j]
        
        if max_sum < sumv:
            max_sum = sumv

    return max_sum

T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    print(f'#{t} {two()}')

