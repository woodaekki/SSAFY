import sys
sys.stdin = open("1.txt", "r")

def recur(stop, remain, cnt):
    global min_cnt
    # 가지치기
    if cnt >= min_cnt:
        return

    if remain < 0:
        return

    if stop == n:
        min_cnt = min(min_cnt, cnt)
        return

    # 충전을 할지 (교체이므로 잔여량 고려 x)
    recur(stop+1, arr[stop]-1, cnt + 1)
    # 출전을 하지 말지
    recur(stop+1, remain-1, cnt)

T = int(input())
for t in range(1, T+1):
    ar = list(map(int, input().split()))
    n = ar[0]
    arr = [0] + ar[1:]
    min_cnt = float('inf')
    recur(1, arr[1], 0)
    print(f'#{t} {min_cnt}')