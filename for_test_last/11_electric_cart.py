import sys
sys.stdin = open("1.txt", "r")

def recur(row, total, cnt):
    global min_battery
    if cnt == n-1:
        min_battery = min(min_battery, total+arr[row][0]) # 다시 사무실로 돌아올때 최소량 구하기
        return

    for factory in range(1,n):
        if not visited[factory]:
            visited[factory] = True
            recur(factory, total+arr[row][factory], cnt+1)
            visited[factory] = False

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    min_battery = float('inf')
    visited[0] = True
    recur(0, 0, 0)
    print(min_battery)


