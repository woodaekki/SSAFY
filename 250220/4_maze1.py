import sys
sys.stdin = open("maze1.txt", "r")

# 1은 벽 / 0은 길 / 3은 도착점
def maze1():

    return arr


T = 10
for t in range(1, T+1):
    tc = int(input())
    arr = [list(input()) for _ in range(16)]

    # 출발점인 2 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == "2":


    print(f'#{t} {maze1()}')