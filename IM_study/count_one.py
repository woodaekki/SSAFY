import sys
sys.stdin = open("1.txt", "r")

def solve():
    cnt = 0
    max_cnt = 0
    for i in range(n):
        if int(arr[i]) == 1:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 0
    # 끝까지 1인 경우
    max_cnt = max(max_cnt, cnt)
    return max_cngit rm --cached 03-pjt

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(input())
    result = solve()
    print(f'#{t} {result}')