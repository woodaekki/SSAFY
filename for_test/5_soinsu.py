import sys
sys.stdin = open("soinsu.txt", "r")

def soinsu(n):
    a = b = c = d = e = 0
    while n % 11 == 0:
        e += 1
        n //= 11
    while n % 7 == 0:
        d += 1
        n //= 7
    while n % 5 == 0:
        c += 1
        n //= 5
    while n % 3 == 0:
        b += 1
        n //= 3
    while n % 2 == 0:
        a += 1
        n //= 2
    return a, b, c, d, e

T = int(input())
for t in range(1, T+1):
    n = int(input())
    result = soinsu(n)
    print(f'#{t} {result[0]} {result[1]} {result[2]} {result[3]} {result[4]}')
    