import sys
sys.stdin = open("1.txt", "r")

"""
1. 최대값 찾아서 
2. 그 이전 가격까지 매수해서, 최댓값에서 매수
3. 최댓값까지 삭제하고, 그 다음 인덱스부터 다시 최댓값 찾아서 다시 매매 반복
4. 가격 리스트 빌 때까지
"""
from collections import deque

def millionaire():
    margin = 0
    prices_deque = deque(prices)  
    while len(prices_deque) > 0:
        # 최댓값 찾아서 
        max_v = max(prices_deque)
        max_idx = prices_deque.index(max_v)

        # 최댓값 이전까지 사기 
        buy = sum(list(prices_deque)[:max_idx])
        sell = max_v * max_idx
        margin += sell - buy

        for _ in range(max_idx + 1): # 최댓값 인덱스까지 삭제, 그 다음 인덱스부터 다시 최댓값 찾고.. 반복 
            if len(prices_deque) > 0:
                prices_deque.popleft()  
            else:
                break
    return margin

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    print(f'#{t} {millionaire()}')