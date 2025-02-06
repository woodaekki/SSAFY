# 가장 높은 곳에서 가장 낮은 곳으로 상자를 이동시킴
# 제한 횟수만큼 반복
# 최고높이 - 최저높이

import sys
sys.stdin = open("input.txt", "r")

T = 10
for t in range(1, T + 1):
    times = int(input()) # 덤프 횟수 제한
    arr = list(map(int, input().split())) # 상자 높이 리스트

    # 1. 리스트를 돌며 가장 높은 곳과 낮은 곳의 상자 높이를 찾는다.
    # 2. 가장 높은 곳의 + 1, 가장 낮은 곳의 -1로 상자를 이동시킨후 리스트를 반환한다.
    # 3. 다시 가장 높은 곳과 낮은 곳을 찾고, 상자를 이동시킨다.
    # 4. times 횟수 만큼 반복한다.
    # 5. 반복문에서 빠져나와 최고높이 - 최저높이를 출력한다.
    max_h = 0 # 가장 높은 곳
    min_h = 999 # 가장 낮은 곳

    for _ in range(times):
        max_idx = 0
        min_idx = 0
        for i in range(1, 100): #처음부터 리스트 끝까지 순회한다.
            # 가장 높은 박스
            if arr[max_idx] < arr[i]:
                max_idx = i
            # 가장 낮은 박스
            if arr[min_idx] > arr[i]:
                min_idx = i

        arr[max_idx] -= 1
        arr[min_idx] += 1

    print(f'#{t} {max(arr)-min(arr)}')

