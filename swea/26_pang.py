import sys
sys.stdin = open("pang.txt", "r")

def pang():
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]  # n줄

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {pang()}')