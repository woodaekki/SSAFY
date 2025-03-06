import sys
sys.stdin = open("password.txt","r")

def password():
    return arr

T = int(input())
for t in range(1,T+1):
    n, m = list(map(int, input().split()))
    arr = [list(input()) for _ in range(n)]
    result = password()
    print(f'#{t} {result}')
