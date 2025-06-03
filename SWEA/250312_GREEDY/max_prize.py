def recur(cnt):
    global max_total
    if cnt == change:
        result = int("".join(arr))
        max_total = max(max_total, result)
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
    arr = list(ar[0])
    change = int(ar[1])
    visited = [[] for _ in range(10)]
    max_total = float('-inf')
    recur(0)
    print(f'#{t} {max_total}')