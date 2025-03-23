import sys
sys.stdin = open("1.txt", "r")

def recur(cnt):
    global max_num
    if cnt == change:
        result = int("".join(card))
        max_num = max(max_num, result)
        return

    n = len(card)
    for i in range(n-1):
        for j in range(i+1, n):
            card[i], card[j] = card[j], card[i] # 교환
            result = int("".join(card))
            if result not in visited[cnt]:
                visited[cnt].append(result)
                recur(cnt+1)
            card[i], card[j] = card[j], card[i] # 원복

T = int(input())
for t in range(1, T + 1):
    card, change = input().split()
    card = list(card)
    change = int(change)
    max_num = float("-inf")
    visited = [[] for _ in range(10)] # 최대 교환횟수 10회
    recur(0)
    print(f'#{t} {max_num}')