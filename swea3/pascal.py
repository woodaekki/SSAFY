import sys
sys.stdin = open("pascal.txt", "r")

def pascal(n):
    pass

T = int(input())
for t in range(1, T+1):
    n = int(input())
    print(f'#{t} {pascal(n)}')