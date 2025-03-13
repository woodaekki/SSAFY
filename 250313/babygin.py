import sys
sys.stdin = open("baby.txt", "r")

# run: 연속한 숫자 / triplet: 같은 숫자
# 베이비진 판단하는 함수
def winner(cards):
    n = len(cards)
    # triplet (똑같은 숫자 3개)
    for i in range(n-2):
        if cards[i] >= 3:
            return True

    # run: (연속된 숫자 3개)
    for i in range(n-2):
        if cards[i] > 0 and cards[i+1] > 0 and cards[i+2] > 0:
            return True
    return False

# 카드 번갈아 담는 함수
# 예외 케이스 !!!!!!)
# 1 1 2 2 2 2 3 3 5 5 7 7 9 9

# 카운팅 정렬을 쓰자 !!!!
def baby(arr):
    player1 = [0]*10
    player2 = [0]*10
    for i in range(len(arr)):
        # player1은 짝수 덱
        if i % 2 == 0:
            player1[arr[i]] += 1
            if winner(player1):
                return 1
        # player2는 홀수 덱
        else:
            player2[arr[i]] += 1
            if winner(player2):
                return 2
    return 0 # 무승부

T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    result = baby(arr)
    print(f"#{t} {result}")