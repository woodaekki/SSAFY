import sys
sys.stdin = open("two.txt", "r")

def two():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if len(a) > len(b):
        a, b = b, a # A를 항상 더 짧은 리스트로

    max_v = -999999999999
    for i in range(len(b) - len(a) + 1):
        sumv = 0 # 현재 합계
        for j in range(len(a)):
            sumv += a[j] * b[i+j]
        if sumv > max_v:
            max_v = sumv
    return max_v

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {two()}')