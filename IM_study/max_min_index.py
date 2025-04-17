import sys
sys.stdin = open("1.txt", "r")

def solve():
    maxv = float('-inf')
    minv = float('inf')

    max_idx = min_idx = 0
    for i in range(n):
        if arr[i] > maxv:
            maxv = arr[i]
            max_idx = i
        elif arr[i] == maxv and i > max_idx:
            max_idx = i
        if arr[i] < minv:
            minv = arr[i]
            min_idx = i
        elif arr[i] == minv and i < min_idx:
            min_idx = i
    return abs(max_idx-min_idx)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve()
    print(f'#{t} {result}')