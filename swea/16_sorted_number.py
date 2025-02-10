import sys
sys.stdin = open("sorted_num.txt", "r")

T = int(input())

def selection_sort():
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

for t in range(1, T+1):
    result = selection_sort()
    print(f'#{t}', end = " ")
    print(*result)