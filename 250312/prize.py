import sys
sys.stdin = open("7.txt", "r")

def change(k):
    global result
    n = len(cards)

    # numbers = int("".join(cards))
    # k번째 depth 에 이미 나온 수이면 반환
    # 아니면 k번째에 잘 저장

    if k == change_cnt:
        numbers = int("".join(cards))
        result = max(result, numbers)
        return

    for i in range(n-1):
        for j in range(i+1, n):
            # 데이터 교환
            cards[i], cards[j] = cards[j], cards[i]
            change(k+1)
            # 원복
            cards[i], cards[j] = cards[j], cards[i]

# 백트래킹: 같은 깊이의 같은 수가 나오면 가지를 치자.

T = int(input())
for t in range(1, T+1):
    cards, change_cnt = input.split()
    change_cnt = int(change_cnt)
    cards = list(cards)