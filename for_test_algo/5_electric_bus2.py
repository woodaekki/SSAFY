import sys
sys.stdin = open("2.txt", "r")

def recur(stop, remain, cnt):
    global min_cnt
    if cnt >= min_cnt:
        return

    if remain < 0:
        return

    # 종점애 도달하면
    if stop == n:
        min_cnt = min(min_cnt, cnt)
        return

    # 충전 교체 o
    recur(stop+1, arr[stop]-1, cnt+1)
    # 충전 교체 x
    recur(stop+1, remain-1, cnt)

T = int(input())
for t in range(1, T+1):
    ar = list(map(int, input().split()))
    n = ar[0]
    arr = [0] + ar[1:]
    min_cnt = float('inf')
    recur(1, arr[1], 0)
    print(f'#{t} {min_cnt}')