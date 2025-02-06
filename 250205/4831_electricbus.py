import sys
sys.stdin = open("elec.txt", "r")

T = int(input())

for t in range(1, T + 1):
    k, n, m = list(map(int, input().split())) # 이동 가능거리, 총 정류장 수, 총 충전소 수
    arr = list(map(int, input().split())) # 충전기 설치된 정류장 번호

    curr = 0 # 현재 위치
    count = 0 # 충전 횟수
    # 1. while curr < n까지 진행
    # 2. 현재 위치에서 이동 가능거리만큼 간다.
    # 3. 이동한 위치에 충전소가 있으면 이동하고 충전 1증가
    # 4. 이동한 위치에 충전소가 없으면 한 칸 전으로 이동, 그 위치가 현재 위치로 갱신, 충전 횟수 1증가
    # 5. 근데 한 칸 전으로 이동했음에도 충전소가 없으면, 0을 충전한다.

    while curr < n:
        if curr + k:
            if curr + k == arr:
                count += 1
                curr = curr + k
            if curr + k != arr:
                curr = curr + k - 1
                count += 1
                if curr + k - 1 == arr:
                    count = 0
    print(count)
