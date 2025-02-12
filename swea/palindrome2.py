import sys
sys.stdin = open("palin2.txt", "r")

def palindrome2():
    m = int(input()) # 찾아야 하는 회문의 길이
    arr = [list(input()) for _ in range(8)]

    cnt = 0  # 찾아야 하는 길이에 맞는 회문일 때

    # 가로로 회문일 때
    for i in range(0, 8):
        for j in range(0, 8-m+1):
            scope = arr[i][j:j+m]
            if scope == scope[::-1]:
                cnt += 1

    # 세로로 회문일 때
    for j in range(0, 8):
        for i in range(0, 8-m+1):
            for k in range(m):
                scope = arr[i:i+k][j]
                if scope == scope[::-1]:
                    cnt += 1

    return cnt


T = 1
for t in range(1, T+1):
    print(f'#{t} {palindrome2()}')
