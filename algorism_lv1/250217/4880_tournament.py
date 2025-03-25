import sys
sys.stdin = open("tournament.txt", "r")

# w1 과 w2 가위바위보 게임을 하여 이긴 사람을 return 한다.
def cal(w1, w2):
    if w1 > w2:
        return w1
    elif w1 <= w2:
        return w2

def game(left, right):
    if left == right:
        return left
    m = (left+right)//2
    winner1 = game(left, right)
    winner2 = game(m+1, right)

    return cal(winner1, winner2)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    print(f'#{t} {game(0, n)}')