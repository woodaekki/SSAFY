def atm():
    n = int(input())
    arr = list(map(int, input().split()))

    waiting = sorted(arr)
    sumv = sumv2 = 0
    for wait in waiting:
        sumv += wait
        sumv2 += sumv
    return sumv2

print(atm())