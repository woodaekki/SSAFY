import sys
sys.stdin = open("1.txt", "r")

def recur(i, j, total):
    global min_sum
    # 이미 총합이 최소합을 넘었다면 반환
    if total >= min_sum:
        return

    # 종료 조건
    if i == n-1 and j == n-1:
        min_sum = min(min_sum, total + arr[i][j])
        return

    # 오른쪽으로
    if j+1 < n:
        recur(i, j+1, total + arr[i][j])
    # 아래로
    if i+1 < n:
        recur(i+1, j, + total + arr[i][j])

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = float("inf")
    recur(0, 0, 0)
    print(f'#{t} {min_sum}')