import sys
sys.stdin = open("1012.txt", "r")

def cabbage():

    return arr

T = int(input())

for t in range(1, T+1):
    m, n, k = list(map(int, input().split())) # 가로, 세로, 배추 총 개수
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = list(map(int, input().split()))
        arr[i][j] = 1 # 배추 위치 저장

result = cabbage()
print(result)