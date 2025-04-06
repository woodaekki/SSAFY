def winner(cards):
    m = len(cards)
    for j in range(m-2):
        if cards[j] > 0 and cards[j+1] > 0 and cards[j+2] > 0:
            return True
        if cards[j] >= 3:
            return True
    return False

def babygin(arr):
    player1 = [0] * 10
    player2 = [0] * 10

    for i in range(len(arr)):
        if i % 2 == 0:
            player1[arr[i]] += 1
            if winner(player1):
                return 1
        else:
            player2[arr[i]] += 1
            if winner(player2):
                return 2
    return 0

T = int(input())
for t in range(1, T+1):
    arr= list(map(int, input().split()))
    result = babygin(arr)
    print(f'#{t} {result}')
