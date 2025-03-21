import sys
sys.stdin = open("two.txt", "r")

def two_sum(n, arr, x):
    start = 0
    end = n-1
    cnt = 0
    while start < end:
        if arr[start] + arr[end] > x:
            end -= 1
        elif arr[start] + arr[end] < x:
            start += 1
        else:
            start += 1
            cnt += 1
    return cnt

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
x = int(input())
result = two_sum(n, arr, x)
print(result)