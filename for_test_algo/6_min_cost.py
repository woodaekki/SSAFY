import sys
sys.stdin = open("2.txt", "r")

def recur(product, total):
    global min_cost
    # 가지치기
    if total >= min_cost:
        return

    if product == n:
        min_cost = min(min_cost, total)
        return

    for factory in range(n):
        if not visited[factory]:
            visited[factory] = True
            recur(product+1, total+arr[factory][product])
            visited[factory] = False

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_cost = float('inf')
    visited = [False] * (n+1)
    recur(0, 0)
    print(f'#{t} {min_cost}')