import sys
sys.stdin = open("paper.txt","r")

def paper(a,b,c,d,color,arr):
    for i in range(a,c+1):
        for j in range(b, d+1):
            arr[i][j] += color

    cnt = 0
    for a in range(10):
        for b in range(10):
            if arr[a][b] == 3:
                cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [[0]*10 for _ in range(10)]
    for _ in range(n):
        a,b,c,d,color = list(map(int, input().split()))
        result = paper(a,b,c,d,color,arr)
    print(f'#{t} {result}')
