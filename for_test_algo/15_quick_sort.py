import sys
sys.stdin = open("2.txt", "r")


def dividing(left, right):
    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and pivot <= arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = dividing(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot+1, right)


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, n - 1)
    print(arr)
