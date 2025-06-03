def solve():
    max_fly = float('-inf')
    for i in range(n-m+1):
        for j in range(n-m+1):
            fly = 0
            for k in range(i, i+m):
                for l in range(j, j+m):
                    fly += arr[k][l]
            max_fly = max(max_fly, fly)
    return max_fly
 
T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = solve()
    print(f'#{t} {result}')