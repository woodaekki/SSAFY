import sys
sys.stdin = open("1.txt", "r")

def solve():
    max_cnt = max_cnt2 = float('-inf')
    # 가로
    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
        # 끝까지 1인 경우
        max_cnt = max(max_cnt, cnt)

    for l in range(m):
        cnt2 = 0
        for k in range(n):
            if arr[k][l] == 1:
                cnt2 += 1
            else:
                max_cnt2 = max(max_cnt2, cnt2)
                cnt2 = 0
        max_cnt2 = max(max_cnt2, cnt2)
    return max(max_cnt, max_cnt2)

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = solve()
    print(f'#{t} {result}')