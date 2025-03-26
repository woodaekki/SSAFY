import sys
sys.stdin = open("1.txt", "r")

def winner(cards):
    n = len(cards)
    # run: 연속한 숫자 3개
    for j in range(n-2):
        if cards[j] > 0 and cards[j+1] > 0 and cards[j+2] > 0:
            return True

    # triplet: 똑같은 숫자 3개
    for k in range(n-2):
        if cards[k] >= 3:
            return True
    return False

def baby():
    player1 = [0]*10
    player2 = [0]*10
    for i in range(len(arr)):
        # player1
        if i % 2 == 0:
            player1[arr[i]] += 1
            if winner(player1):
                return 1

        # player2
        else:
            player2[arr[i]] += 1
            if winner(player2):
                return 2
    return 0


T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f'#{t} {baby()}')