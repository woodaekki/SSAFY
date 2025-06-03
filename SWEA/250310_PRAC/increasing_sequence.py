def solve():
    cnt = 0
    max_cnt = float('-inf')
    for i in range(n-1):
        num = arr[i]
        for j in range(i+1, n):
            if num < arr[j]:
                cnt += 1
                num = arr[j]
        max_cnt = max(max_cnt, cnt)
        cnt = 0
    max_cnt = max(max_cnt, cnt)
    return max_cnt
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve()
    print(f'#{t} {result}')