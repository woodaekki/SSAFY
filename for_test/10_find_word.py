import sys
sys.stdin = open("word_find.txt", "r")

def find():
    leng = 0
    cnt = 0
    # 가로줄 
    for i in range(n):
        leng = 0
        for j in range(n):
            if arr[i][j] == 1:
                leng += 1
            if arr[i][j] == 0:
                if leng == k:
                    cnt += 1
                leng = 0
        if leng == k:
            cnt += 1
    
    # 세로줄
    for j in range(n):
        leng = 0
        for i in range(n):
            if arr[i][j] == 1:
                leng += 1
            if arr[i][j] == 0:
                if leng == k:
                    cnt += 1
                leng = 0
        if leng == k:
            cnt += 1

    return cnt

T = int(input())
for t in range(1, T+1):
    n, k = list(map(int, input().split())) # nxn배열, k는 찾는 길이 
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{t} {find()}')