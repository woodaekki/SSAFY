def solve():
    for i in range(len(arr)):
        if arr[i] == 'd':
            arr[i] = 'b'
        elif arr[i] == 'b':
            arr[i] = 'd'
        elif arr[i] == 'p':
            arr[i] = 'q'
        elif arr[i] == 'q':
            arr[i] = 'p'
    return arr
 
T = int(input())
for t in range(1, T+1):
    arr = list(input())
    result = solve()
    print(f'#{t}', end = " ")
    for j in range(len(arr)-1, -1, -1):
        print(arr[j], end="")
    print()