import sys
sys.stdin = open("2.txt", "r")

def space():
    return arr

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = space()
    print(f'#{t} {result}')