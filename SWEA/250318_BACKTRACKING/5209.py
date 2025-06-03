def recur(row, total):
    global min_cost
    if total >= min_cost:
        return
 
    if row == n:
        min_cost = min(min_cost, total)
        return
 
    for factory in range(n):
        if not visited[factory]:
            visited[factory] = True
            recur(row+1, total+arr[row][factory])
            visited[factory] = False
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    min_cost = float('inf')
    recur(0, 0)
    print(f'#{t} {min_cost}')