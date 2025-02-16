# 최대값을 구하는 함수
def max_product(A, B):
    if len(A) > len(B):
        A, B = B, A # A를 항상 더 짧은 리스트로

    max_v = float('-inf') # 최대값 초기화(음의 무한대)
    for i in range(len(B) - len(A) + 1):
        current_sum = 0 # 현재 합계
        for j in range(len(A)): # A가 항상 짧기 때문에
            current_sum += A[j] * B[i+j] # 누적
        max_v = max(max_v, current_sum)

    return max_v


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 최대값 계산 ---> 함수호출(max_v가 리턴되서 result에 할당)
    result = max_product(A, B)
    print(f'#{tc} {result}')