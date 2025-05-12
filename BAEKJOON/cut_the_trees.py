import sys
sys.stdin = open("1.txt", "r")

def solve():
    left, right = 0, arr[-1]
    result = 0
    while left <= right:
        mid = (left + right) // 2
        sumv = 0
        for i in range(n):
            if arr[i] - mid > 0:
                sumv += arr[i] - mid
            else:
                pass
        if sumv >= m:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(solve())