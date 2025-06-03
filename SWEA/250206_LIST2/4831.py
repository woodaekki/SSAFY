# 1. while curr + k < n까지 진행
# 2. 현재 위치에서 이동 가능거리만큼 최대한 간다.
# 3. 현재위치보다 1칸 이상 최대한 이동했는데 충전소가 없으면 계속 1칸씩 뒤로 감
# 4. 계속 뒤로 가다가 현재 위치가 되면 0
# 5. 충전 후 curr 갱신 / 카운트 1증가
 
T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    k, n, m = map(int, input().split())  # 이동 가능 거리, 총 정류장 수, 총 충전소 수
    arr = list(map(int, input().split()))  # 충전기 설치된 정류장 번호 (집합으로 저장하여 탐색 속도 향상)
     
    curr = 0  # 현재 위치
    count = 0  # 충전 횟수
     
    while curr + k < n:  # 마지막 정류장 도달할 때까지지
        nex = curr + k  # 이동 가능한 거리
        while nex > curr and nex not in arr: # 이동할 거리가 현재 위치보다 근데 충전소가 없으면 
            nex -= 1  # 한 칸씩 이전으로 이동
         
        if nex == curr: # 이동할 거리가 현재 위치가 되면 0 반환하고 멈춤
            count = 0
            break
         
        curr = nex  # 충전소에서 충전 후 이동
        count += 1
     
    print(f"#{t} {count}")