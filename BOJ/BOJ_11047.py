def vending_machine():
    n, k = list(map(int, input().split())) # 동전개수, 가진 돈
    ar = []
    for _ in range(n):
        coin = int(input())
        ar.append(coin)
        arr = sorted(ar, reverse = True)

    cnt = 0
    for money in arr:
        change1 = k // money
        change2 = k % money
        cnt += change1
        k = change2
    return cnt 

print(vending_machine())

