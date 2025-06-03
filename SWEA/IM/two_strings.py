def solve():
    max_total = float('-inf')
    len_a = min(len(a), len(b))
    len_b = max(len(a), len(b))
 
    for i in range(len_b - len_a + 1):
        sumv = 0  # 현재 합계
        for j in range(len_a):
            sumv += a[j] * b[i + j]
        max_total = max(max_total, sumv)
 
    return max_total
 
 
T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    if n < m:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
    else:
        b = list(map(int, input().split()))
        a = list(map(int, input().split()))
    result = solve()
    print(f'#{t} {result}')