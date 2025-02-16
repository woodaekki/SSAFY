import sys
sys.stdin = open("flatten.txt", "r")

def flatten(times, arr):
    while times != 0:
        for i in range(0, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        arr[-1] -= 1
        arr[0] += 1
        times -= 1

    for i in range(0, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
    return arr[-1] - arr[0]
    
T = 10
for t in range(1, T+1):
    times = int(input()) # 덤프횟수
    arr = list(map(int, input().split()))
    print(f'#{t} {flatten(times, arr)}')