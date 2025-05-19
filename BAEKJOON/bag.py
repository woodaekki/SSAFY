def solve():
    dp = [0] * (k + 1)  # 무게가 0부터 K까지 가능하므로
    for w, v in arr:
        for j in range(k, w - 1, -1): # 큰 무게부터
            dp[j] = max(dp[j], dp[j - w] + v) # 물건을 선택하지 않는 경우, 선택하는 경우 중 최대값

    return dp[k]

n, k = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)] # 무게, 가치
# print(arr)
result = solve()
print(result)

