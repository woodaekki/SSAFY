import sys
sys.stdin = open("7.txt", "r")

def change(k, n):
    global maxv
    if k == n: # 모든 교환이 끝난 경우 
        tmp = int("".join(card))
        if maxv < tmp:
            maxv = tmp
    else:
        for i in range(m-1): # 왼쪽 카드
            for j in range(i+1, m): # 오른쪽 카드 
                # (교환횟수, 만들어지는 값을 저장해서 중복 방지)
                card[i], card[j] = card[j], card[i] # 카드 교환
                # 가지 치기 
                tmp = int("".join(card)) 
                # 만들어진적이 없으면 
                if tmp not in memo[k]:
                    memo[k].append(tmp)
                    change(k+1, n)
                card[i], card[j] = card[j], card[i] # 원상복구 

T = int(input())
for t in range(1, T+1):
    card, n = input().split()
    card = list(card)
    n = int(n)
    m = len(card)
    maxv = 0
    memo = [[] for _ in range(10)] # 최대 교환횟수가 10
    change(0, n)
    print(f'#{t} {maxv}')