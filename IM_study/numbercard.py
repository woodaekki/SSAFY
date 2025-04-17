import sys
sys.stdin = open("1.txt", "r")

def solve():
    cards = {}
    for i in range(n):
        if arr[i] not in cards:
            cards[(arr[i])] = 1
        elif arr[i] in cards:
            cards[(arr[i])] += 1

    max_k = max_t = 0
    for key, item in cards.items():
        if item > max_t:
            max_t = item
            max_k = int(key)
        # 카드 장수가 같을 경우에는 적힌 숫자가 큰 쪽을 선택
        elif item == max_t:
            if int(key) > max_k:
                max_t = item
                max_k = int(key)
    return max_k, max_t

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(input())
    result = solve()
    print(f'#{t} {result[0]} {result[1]}')