import sys
sys.stdin = open("1.txt", "r")

def solve():
    cnt = 0
    for i in range(n):
        if a[i] != b[i]:
            cnt += 1
            for j in range(i, n):
                a[j] = 1- a[j]
    return cnt

T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = solve()
    print(f'#{t} {result}')

