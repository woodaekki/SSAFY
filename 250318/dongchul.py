import sys
sys.stdin = open("chul.txt", "r")

def recur():


T = int(input())
for t in range(1, T+1):
    n = int(input())
    for _ in range(n):
        arr = list(map(int, input().split()))

    print(f'#{t}')