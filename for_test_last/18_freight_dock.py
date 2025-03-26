import sys
sys.stdin = open("1.txt", "r")

def solve():
    start, end = arr[0]
    cnt = 1 # 첫 화물 적재
    for i in range(1,n):
        if arr[i][0] >= end:
            cnt += 1
            start, end = arr[i]
    return cnt

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        start, end = list(map(int, input().split()))
        arr.append((start, end))
    arr.sort(key= lambda x:x[1])
    result = solve()
    print(f'#{t} {result}')
