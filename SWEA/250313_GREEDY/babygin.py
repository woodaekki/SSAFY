def winner(cards):
    m = len(cards)
    # run: 연속
    for j in range(m-2):
        if cards[j] >= 1 and cards[j+1] >= 1 and cards[j+2] >= 1:
            return True
 
    # triplet: 같은숫자
    for k in range(m):
        if cards[k] >= 3:
            return True
    return False
 
def babygin(arr):
    player1 = [0] * 10
    player2 = [0] * 10
 
    for i in range(len(arr)):
        # player1 카드 배분 받기 (짝수번째 카드)
        if i % 2 == 0:
            player1[arr[i]] += 1
            if winner(player1):
                return 1
        # player2 카드 배분 받기 (홀수번째 카드)
        if i % 2 == 1:
            player2[arr[i]] += 1
            if winner(player2):
                return 2
    return 0
 
 
T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    result = babygin(arr)
    print(f'#{t} {result}')