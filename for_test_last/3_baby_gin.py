import sys
sys.stdin = open("1.txt", "r")

# 베이비진 여부
def winner(cards):
    n = len(cards)
    # run: 연속한 숫자
    for j in range(n-2):
        if cards[j] > 0 and cards[j+1] > 0 and cards[j+2] > 0:
            return True

    # triplet: 같은 숫자
    for k in range(n-2):
        if cards[k] >= 3:
            return True
    return False

# 교대로 카드 뽑기
def pick(arr):
    # 카운팅 배열 생성
    player1 = [0] * 10
    player2 = [0] * 10
    for i in range(len(arr)):
        # player1은 짝수 번째에 뽑기
        if i % 2 == 0:
            player1[arr[i]] += 1
            # print(f"player1의 덱: {player1}")
            if winner(player1):
                return 1
        # player2는 홀수 번째에 뽑기
        else:
            player2[arr[i]] += 1
            # print(f"player2의 덱: {player2}")
            if winner(player2):
                return 2
    return 0 # 무승부

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    result = pick(arr)
    print(f'#{t} {result}')