import sys
sys.stdin = open("maze.txt", "r")

def maze():


    return start



T = int(input())
for t in range(1, T+1):
    n = int(input()) # n x n 배열
    arr = [list(map(int, input().split())) for _ in range(1, T+1)]

    for i in range(n):
        start = arr[i].index(2)
        break
    print(f'#{t} {maze()}')