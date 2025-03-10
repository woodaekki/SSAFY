import sys
sys.stdin = open("1.txt", "r")

def farming(cnt):
    cnt = 0
    s = n//2
    e = n//2
    # 중앙라인을 포함한 마름모 윗부분
    for up in range(0,n//2+1):
        if 0 <= s and e <= n:
            # s에서 e의 합
            cnt += sum(arr[up][s:e+1])
            # print(arr[up][s:e+1])
            s -= 1
            e += 1
            # print(cnt)

    # 마름모 아랫 부분
    cnt2 = 0
    s = n // 2
    e = n // 2
    for down in range(n-1, n//2, -1):
        if 0 < s and e <= n:
            # s에서 e의 합
            cnt2 += sum(arr[down][s:e + 1])
            # print(arr[down][s:e + 1])
            s -= 1
            e += 1
    return cnt + cnt2

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    cnt = 0
    result = farming(cnt)
    print(f'#{t} {result}')
