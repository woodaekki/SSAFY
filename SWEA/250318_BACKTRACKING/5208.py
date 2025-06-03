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
 
    # 배터리를 교체하는 경우
    recur(stop+1, arr[stop]-1, cnt+1)
    # 안하는 경우
    recur(stop+1, remain-1, cnt)
 
 
T = int(input())
for t in range(1, T+1):
    ar = list(map(int, input().split()))
    n = ar[0]
    arr = [0] + ar[1:]
    min_cnt = float('inf')
    recur(1, arr[1], 0)
    print(f'#{t} {min_cnt}')