import sys
sys.stdin = open("1.txt", "r")

def solve():
    lst = []
    left = 0
    right = n-1
    mid = n//2
    if len(arr) % 2 == 0:
        while left < right:
            lst.append(arr[right])
            right -=1
            lst.append(arr[left])
            left += 1
    else:
        while left < right:
            lst.append(arr[right])
            right -=1
            lst.append(arr[left])
            left += 1
        # 남은 하나
        lst.append(arr[mid])
    return lst[:10]


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    result = solve()
    print(f'#{t}', *result)


