import sys
sys.stdin = open("1.txt", "r")

def recur(cnt):
    global max_prize
    if cnt == change:
        total = int("".join(arr))
        max_prize = max(max_prize, total)
        return

    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            arr[i], arr[j] = arr[j], arr[i]
            result = int("".join(arr))
            if result not in visited[cnt]:
                visited[cnt].append(result)
                recur(cnt+1)
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for t in range(1, T+1):
    ar = input().split()
    change = int(ar[1]) # 최대 교환 횟수
    arr = list(ar[0])
    max_prize = float('-inf')
    visited = [[] for _ in range(10)]
    recur(0)
    print(f'#{t} {max_prize}')