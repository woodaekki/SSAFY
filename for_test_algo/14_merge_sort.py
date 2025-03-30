import sys
sys.stdin = open("2.txt", "r")

# 병합
def merging(left, right):
    result = [0] * (len(left)+len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1
    while r < len(right):
        result[l + r] = right[r]
        r += 1
    return result


# 분할 및 정렬
def merge_sort(ar):
    if len(ar) == 1:
        return ar

    mid = len(ar) // 2
    left = ar[:mid]
    right = ar[mid:]

    a = merge_sort(left)
    b = merge_sort(right)

    merging_lst = merging(a, b)
    return merging_lst

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    final = merge_sort(arr)
    print(final)
    # print(cnt)