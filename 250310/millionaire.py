import sys
sys.stdin = open("1.txt", "r")

def millionaire():
    

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    print(f'#{t} {millionaire()}')