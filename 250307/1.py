def solve():
    # 첫번째 가로 줄의 연속 1 개수를 센다
    # 최대 연속 1 개수에 그 수를 저장한다.
    # 세로줄의 1 개수와 가로줄의 1 개수만큼 되는지 센다.
    # 두번째 가로 줄의 연속 1 개수를 센다.
    # 최대 연속 1개수보다 크면
    # 세로줄의 1개수를 센다.
    # 크지 않으면 세번째 가로 줄의 연속 1 개수를 센다....
    for i in range(n):
        for j in range(m):


n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
result = solve()
print(result)