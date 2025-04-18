import sys
sys.stdin = open("bus.txt", "r")

def recur(stop, remain, cnt):
    global min_cnt
    # print(stop, remain, cnt)
    # 남은 양이 0 미만이 되는 경우
    if remain < 0:
        return

    # 가지치기
    if cnt >= min_cnt:
        return

    # 종점에 도달하는 경우
    # 종점에 도달했을때 남은 충전량이 0인것은 괜찮음
    if stop == n:
        min_cnt = min(min_cnt, cnt)
        return

    # 현재 정류소에서 충전 안 한 경우
    recur(stop+1, remain-1, cnt)
    # 현재 정류소에서 충전 한 경우
    recur(stop+1, arr[stop]-1, cnt + 1)

T = int(input())
for t in range(1, T+1):
    ar = list(map(int, input().split()))
    n = ar[0]
    arr = [0] + ar[1:]
    min_cnt = float('inf')
    recur(1, arr[1], 0)
    print(f'#{t} {min_cnt}')