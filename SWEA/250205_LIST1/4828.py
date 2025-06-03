def solve():
    maxv = float('-inf')
    minv = float('inf')
 
    for i in range(n):
        if arr[i] > maxv:
            maxv = arr[i]
        if arr[i] < minv:
            minv = arr[i]
    return maxv-minv
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve()
    print(f'#{t} {result}')