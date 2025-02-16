import sys
sys.stdin = open("dol1.txt", "r")

def dol1():
    n, m = list(map(int, input().split())) # 가로줄의 길이, 몇줄 받을 건지지
    arr = list(map(int, input().split()))
    for _ in range(m):
        i, j = list(map(int, input().split()))
        for dol in range(i-1, i-1+j):
            if 0 <= dol < n:
                if arr[dol] == 1:
                    arr[dol] = 0
                if arr[dol] == 0:
                    arr[dol] = 1
        
    return arr

T = int(input())
for t in range(1, T+1):
    result = dol1()
    print(f'#{t}', *result)
        