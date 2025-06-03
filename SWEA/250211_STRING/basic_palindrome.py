def solve():
    n = len(arr)
    for i in range(n//2):
        if arr[i] == arr[n -1-i]:
            return 1
    return 0
 
T = int(input())
for t in range(1, T+1):
    arr = list(input())
    result = solve()
    print(f'#{t} {result}')