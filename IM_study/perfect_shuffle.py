import sys
sys.stdin = open("1.txt", "r")

def solve():
    if n % 2 == 0:
        left = 0
        right = n//2
        while left < n and right < n:
            print(arr[left], end=" ")
            left += 1
            print(arr[right], end=" ")
            right += 1
    else:
        left = 0
        mid = (n+1) //2
        right = (n+1)//2
        while left < n and right < n:
            print(arr[left], end=" ")
            left += 1
            print(arr[right], end=" ")
            right += 1
        # 하나 남은게 더 있다면
        if left != mid:
            print(arr[left], end = " ")


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(str, input().split()))
    print(f'#{t}', end = " ")
    solve()
    print()


