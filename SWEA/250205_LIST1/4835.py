def solve():
    maxv = float('-inf')
    minv = float('inf')
 
    for i in range(n-m+1):
        scope = arr[i:i+m]
        sumv = sum(scope)
        if sumv > maxv:
            maxv = sumv
        if sumv < minv:
            minv = sumv
    return maxv - minv
 
 
T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = solve()
    print(f'#{t} {result}')