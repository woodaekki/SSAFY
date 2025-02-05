T = int(input())

for t in range(1, T + 1):
    k, n, m = list(map(int, input().split())) # 이동 가능거리, 총 정류장 수, 충전 정류소 수
    arr = list(map(int, input().split())) # 충전기 설치된 정류장 번호

    arr = [0] + arr + [n] # 충전기 설치된 번호는 처음과 마지막 정류장을 포함해야함
    curr = 0 # 현재 위치
    count = 0 # 충전 횟수
    
    for i in range(0, len(arr) - 1):
        # 다음 충전소가 현재기준 이동거리보다 멀다면, 그 이전 충전소로 이동
        if arr[i + 1] > curr + k:
            curr = arr[i] # 이전 충전소가 현재 위치가 됨
            count += 1 # 충전 횟수 증가
    
    print(f'#{t} {count}')
T = int(input())

for t in range(1, T + 1):
    k, n, m = list(map(int, input().split())) # 이동 가능거리, 총 정류장 수, 충전 정류소 수
    arr = list(map(int, input().split())) # 충전기 설치된 정류장 번호

    arr = [0] + arr + [n] # 충전기 설치된 번호는 처음과 마지막 정류장을 포함해야함
    curr = 0 # 현재 위치
    count = 0 # 충전 횟수
    
    while curr < n:
        nex = curr
        for i in range(0, len(arr) - 1):
            # 충전소 리스트를 보고, 갈 수 있는 가장 마지막 충전소로 이동
            if arr[i + 1] > curr + k:
                nex = arr[i] # 마지막 충전소로 이동
                count += 1 # 충전 횟수 증가
        if nex == curr:
            break
        
    print(f'#{t} {count}')



