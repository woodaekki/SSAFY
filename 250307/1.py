def solve():
    # 첫번째 가로 줄의 연속 1 개수를 센다
    # 세로줄의 1 개수와 가로줄의 1 개수만큼 되는지 센다.


n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
result = solve()
print(result)