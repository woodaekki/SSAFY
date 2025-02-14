import sys
sys.stdin = open("idx.txt", "r")

def idx():
    maxv = -99999999999
    minv = 9999999999
    max_idx = min_idx = 0
    for i in range(n):
        if arr[i] >= maxv:
            maxv = arr[i]
            max_idx = i
        if arr[i] < minv:
            minv = arr[i]
            min_idx = i

    diff = max_idx - min_idx
    if diff < 0:
        diff = -diff
    return diff


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{t} {idx()}')