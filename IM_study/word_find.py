import sys
sys.stdin = open("1.txt", "r")

def solve():
    max_cnt = 0
    # 가로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    max_cnt += 1
                cnt = 0
        if cnt == k:
            max_cnt += 1
            cnt = 0


    # 세로
    max_cnt2 = 0
    for j in range(n):
        cnt2 = 0
        for i in range(n):
            if arr[i][j] == 1:
                cnt2 += 1
            else:
                if cnt2 == k:
                    max_cnt2 += 1
                cnt2 = 0

        if cnt2 == k:
            max_cnt2 += 1
            cnt2 = 0

    return max_cnt + max_cnt2

T = int(input())
for t in range(1, T+1):
    n, k = list(map(int, input().split())) # 가로세로 / 단어의 길이
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = solve()
    print(f'#{t} {result}')