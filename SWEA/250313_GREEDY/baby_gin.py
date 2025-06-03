def winner(cards):
    m = len(cards)
    for j in range(m-2):
        if cards[j] > 0 and cards[j+1] > 0 and cards[j+2] > 0:
            cards[j] -= 1
            cards[j + 1] -= 1
            cards[j + 2] -= 1
            return True
    for k in range(m):
        if cards[k] >= 3:
            cards[k] -= 3
            return True
 
def babygin(arr):
    player = [0] * 10
    total = 0
    for i in range(len(arr)):
        player[int(arr[i])] += 1
        if winner(player):
            total += 1
 
    if total >= 2:
        return 'true'
    else:
        return 'false'
 
T = int(input())
for t in range(1, T+1):
    arr = list(input().strip())
    print(f'#{t} {babygin(arr)}')