import sys
sys.stdin = open("1.txt", "r")

def solve():
    cnt = i = 0
    while i < len(a):
        b_scope = b[:len(b)]
        if a[i:len(b)+i] == b_scope:
            i += len(b)
            cnt += 1
        else:
            i += 1
            cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    a, b = input().split()
    result = solve()
    print(f'#{t} {result}')
