def solve():
    start, end = arr[0]
    cnt = 1
 
    for i in range(n):
        if arr[i][0] >= end:
            start, end = arr[i]
            cnt += 1
    return cnt
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        s, e = list(map(int, input().split()))
        arr.append((s, e))
    arr.sort(key=lambda x:x[1])
    # print(arr)
    print(f'#{t} {solve()}')