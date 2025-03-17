import sys
sys.stdin = open("5205.txt", 'r')

def dividing(left, right):
    pivot = arr[left] # 피벗은 항상 가장 왼쪽 원소
    i = left + 1 # 피벗 다음 원소부터 
    j = right # 가장 오른쪽 원소부터 

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
    
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[left], arr[j] = arr[j], arr[left]
    return j # j가 피벗이 된다.


def quick_sort(left, right):
    if left < right:
        pivot = dividing(left, right)
        quick_sort(left, pivot-1)
        quick_sort(pivot+1, right)


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, n-1)
    print(f'#{t} {arr[n//2]}')