import sys
sys.stdin = open("1.txt", "r")

def solve():
    max_cnt = -1
    for i in range(0, n-1):
        cnt = 0
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                cnt += 1
                print(arr[i], arr[j])
                print(cnt)
        max_cnt = max(max_cnt, cnt)
    return max_cnt

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve()
    print(f'#{t} {result}')