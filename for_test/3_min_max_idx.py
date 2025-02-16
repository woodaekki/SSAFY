import sys
sys.stdin = open("idx.txt", "r")

def idx(n, arr):
    maxv = -99999999999
    minv = 9999999999
    max_idx = min_idx = 0
    for i in range(n):
        if arr[i] > maxv:
            maxv = arr[i]
            max_idx = i
        if arr[i] < minv:
            minv = arr[i]
            min_idx = i
    # 작은 수가 여러개일경우 먼저 나오는 위치로
    if minv == arr[i]:
        if i < min_idx:
            min_idx = i

    # 큰 수가 여러개일경우 마지막 나오는 위치로
    if maxv == arr[i]:
        if i > max_idx:
            max_idx = i
    
    # 차이에 절댓값 씌우기
    diff = max_idx - min_idx
    if diff < 0:
        diff = -diff
    return diff
    


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{t} {idx(n, arr)}')