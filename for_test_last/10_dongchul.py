import sys
sys.stdin = open("1.txt", "r")

def recur(i, total):
    global max_success
    # 가지치기
    if total <= max_success:
        return

    if i == n:
        max_success = max(max_success, total)
        return

    for person in range(n):
        if not visited[person]:
            visited[person] = True
            recur(i+1, total*arr[i][person])
            visited[person] = False


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 확률로 저장하기
    for i in range(n):
        for j in range(n):
            arr[i][j]  = arr[i][j] / 100
    max_success = float('-inf')
    visited = [False] * n
    # 확률은 항상 0부터 1사이의 값이고, 0부터 시작하면 계속 곱해도 0 !!
    recur(0, 1)
    print(f'#{t} {max_success*100:.6f}') # 소수점 6째자리까지