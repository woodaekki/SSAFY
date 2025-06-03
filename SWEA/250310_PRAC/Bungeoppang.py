def fish(m,k,arrivetime):
    arrivetime.sort()
    bread = 0  # 현재까지 만든 붕어빵 개수
    time = 0  # 현재 시간
    idx = 0  # 현재 처리할 손님 인덱스
 
    while idx < n:
        # 손님 도착했을 때
        if arrivetime[idx] == time:
            if bread > 0:  # 붕어빵이 있다면
                bread -= 1
                idx += 1
            else: # 붕어빵 없으면
                return 'Impossible'
        else: # 손님 도착하지 않은 동안
            time += 1  # 시간 증가
            # 붕어빵 만들기
            if time > 0 and time % m == 0:
                bread += k
                # print(bread)
 
    return 'Possible'
 
T = int(input())
for t in range(1,T+1):
    n, m, k = list(map(int, input().split())) # n명, m초의 시간을 들여, k개의 붕어빵
    arr = list(map(int, input().split()))
    arrivetime = sorted(arr)
    print(f'#{t} {fish(m,k,arrivetime)}')