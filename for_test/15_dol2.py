# import sys
# sys.stdin = open("dol2.txt", "r")

def dol2():
    n, m = list(map(int, input().split())) # 가로줄의 길이, 몇줄 받을 건지지
    arr = list(map(int, input().split()))
    for _ in range(m):
        i, j = list(map(int, input().split()))
        for dol in range(0, j+1):
            if 0 <= i-1-dol < n and 0 <= i-1+dol < n:
                if arr[i-1-dol] == arr[i-1+dol]:
                    arr[i-1-dol] = 1 - arr[i-1-dol]
                    arr[i-1+dol] = 1 - arr[i-1+dol]
              
    return arr

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {dol2()}')