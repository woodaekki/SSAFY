import sys
sys.stdin = open("1.txt", "r")

"""
예를 들어 1 1 3 1 2 1일때

1. 숫자가 증가하는 구간 찾기

1,1,3

2.구간의 마지막 숫자와 인덱스+1 저장

그 인덱스 이전 인덱스까지의 합을 구해 3*그 이전 인덱스+1에서 차감

그 값을 margin에 저장하기

3. 또 숫자가 다음 인덱스로 넘어가 증가하는 구간 찾기

1, 2

2.의 과정 반복

3애서 더이상 증가하는 구간이 없으면

1밖에 없음.따라서 멈추고 margin 반환하기
"""

def millionaire():
    margin = 0
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n and prices[j] >= prices[j - 1]:
            j += 1
            # print(j - 1, j)
        
        buy = sum(prices[i:j-1])
        # print(buy)
        sell = prices[j - 1] * (j - i - 1)
        # print(sell)
        margin += sell - buy
        # print(margin)
        i = j  # 다음 구간 시작점으로 이동
        # print(i)

    return margin

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    print(f'#{t} {millionaire()}')