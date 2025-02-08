# 가장 높은 곳에서 가장 낮은 곳으로 상자를 이동시킴
# 제한 횟수만큼 반복
# 최고높이 - 최저높이

import sys
sys.stdin = open("dump.txt", "r")  

T = 10
for t in range(1, T+1):
    times = int(input()) # 덤프횟수
    arr = list(map(int, input().split())) # 각 상자의 높이값
    
    # 가장 높은 상자와 가장 낮은 상자 뽑기
    for _ in range(times):
        maxv = 0
        minv = 0
        for i in range(1, 100):
            if arr[i] > arr[maxv]:
                maxv = i
            if arr[i] < arr[minv]:
                minv = i
        # 가장 높은 상자 -1, 가장 낮은 상자 +1
        arr[maxv] -= 1
        arr[minv] += 1
    
    #times가 끝난 후 가장 높은 상자와 낮은 상자의 차이
    for box in arr:
        if arr[maxv] < box:
            arr[maxv] = box
        if arr[minv] > box:
            arr[minv] = box
    print(f'#{t} {arr[maxv]- arr[minv]}')