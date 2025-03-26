import sys
sys.stdin = open("1.txt", "r")

def recur(stop, remain, cnt):
    global min_change
    n = len(arr)
    if cnt >= min_change:
        return

    if remain < 0:
        return

    if stop == n:
        min_change = min(min_change, cnt)
        return
    # 배터리 교체 o
    recur(stop+1, arr[stop]-1, cnt+1)
    # 배터리 교체 x
    recur(stop+1, remain-1, cnt)

T = int(input())
for t in range(1, T+1):
    ar = list(map(int, input().split()))
    n = ar[0]
    arr = [0]+ar[1:]
    min_change = float('inf')
    recur(1, arr[1], 0)
    print(f'#{t} {min_change}')