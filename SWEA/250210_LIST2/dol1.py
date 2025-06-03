def dol1():
    n, m = list(map(int, input().split())) 
    arr = list(map(int, input().split()))
    for _ in range(m):
        i, j = list(map(int, input().split()))
        for dol in range(i-1, i+j-1):
            if dol < n:
                arr[dol] = arr[i-1]
    return arr
 
T = int(input())
for t in range(1, T+1):
    result = dol1()
    print(f'#{t}', *result)