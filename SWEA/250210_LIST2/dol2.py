def dol2():
    n, m = map(int, input().split()) # 돌의 수, 뒤집기 횟수
    arr = list(map(int, input().split()))
    for _ in range(0, m):
        i, j = map(int, input().split()) # i번째부터 j개의 돌을 i번째 돌의 색을 교체
        i -= 1 # 문제에서 1번째 돌부터 시작하므로
         
        for dol in range(1, j+1):
            if 0 <= i-dol < n and 0 <= i+dol < n: # 범위 벗어나지 않도록
                if arr[i+dol] == arr[i-dol]:
                    if arr[i+dol] == 0:
                        arr[i+dol] = 1
                        arr[i-dol] = 1
 
                    else:
                        arr[i+dol] = 0
                        arr[i-dol] = 0
    return " ".join(map(str, arr))
 
 
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {dol2()}')