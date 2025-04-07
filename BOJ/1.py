import sys
sys.stdin = open('1.txt', 'r')

def solve(cards):
    for i in range(len(arr)-2):
        if int(cards[i]) > 0 and int(cards[i+1]) > 0 and int(cards[i+2]) > 0:
            return 'run'
        if int(cards[i]) >= 3:
            return 'triplet'

def winner():
    player = [0] * 10
    for j in range(len(arr)):
        player[int(arr[j])] += 1
        # print(player)
        if solve(player)== ('run' and 'triplet'):
            return 'true'
        else:
            return 'false'



T = int(input())
for t in range(1, T+1):
    arr = list(input())
    arr.sort()
    # print(arr)
    result = solve(arr)
    print(f'#{t} {result}')
