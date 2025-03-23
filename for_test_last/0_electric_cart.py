import sys
sys.stdin = open("1.txt", "r")

def recur(curr, total, cnt):
    global min_battery
    if cnt == n - 1: # 모든 사무실 다 방문한 경우
        min_battery = min(min_battery, total + arr[curr][0])
        return

    for next_factory in range(1, n):
        if not visited[next_factory]:
            visited[next_factory] = True
            recur(next_factory, total + arr[curr][next_factory], cnt + 1)
            visited[next_factory] = False


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_battery = float('inf')
    visited = [False] * n
    recur(0, 0, 0)
    print(f'#{t} {min_battery}')