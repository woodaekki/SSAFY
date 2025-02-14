import sys
sys.stdin = open("ancient.txt", "r")

def ancient():
    max_leng = max_leng2 = 0
    # 가로 방향
    for i in range(n):
        leng = 0
        for j in range(m):
            if arr[i][j] == 1:
                leng += 1
            if arr[i][j] == 0:
                if leng > max_leng:
                    max_leng = leng
                    leng = 0
        if leng > max_leng: # 끝까지 1일 경우
            max_leng = leng

    # 세로 방향
    for j in range(m):
        leng2 = 0
        for i in range(n):
            if arr[i][j] == 1:
                leng2 += 1
            if arr[i][j] == 0:
                if leng2 > max_leng2:
                    max_leng2 = leng2
                    leng2 = 0
        if leng2 > max_leng2:
            max_leng2 = leng2

    # 가로 최대와 세로 최대 중 더 긴 구조물 길이
    if max_leng > max_leng2:
        return max_leng
    else:
        return max_leng2

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{t} {ancient()}')