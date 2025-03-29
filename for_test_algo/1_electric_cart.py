# import sys
# sys.stdin = open("2.txt", "r")

def recur(curr, total, cnt):
    global min_sum
    if cnt == n-1:
        min_sum = min(min_sum, total+arr[curr][0])
        return

    for factory in range(1, n):
        if not visited[factory]:
            visited[factory] = True
            recur(factory, total+arr[curr][factory], cnt+1)
            visited[factory] = False

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = float('inf')
    visited = [False] * (n+1)
    recur(0, 0, 0)
    print(f'#{t} {min_sum}')