import sys
sys.stdin = open("gugan.txt", "r")

def gugan():
    maxv = -9999999999999
    minv = 99999999999999
    for i in range(n-m+1):
        scope = arr[i:i+m]
        total = 0
        for num in scope:
            total += num
        if maxv < total:
            maxv = total
        if minv > total:
            minv = total
    return maxv - minv

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(f'#{t} {gugan()}')