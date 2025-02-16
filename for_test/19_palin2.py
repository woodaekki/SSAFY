import sys
sys.stdin = open("palin2.txt", "r")

def palin2():
    n, k = list(map(int, input().split()))
    arr = [list(input()) for _ in range(n)]

    # 가로 
    lst = []
    for i in range(n):
        for j in range(n-k+1):
            scope = arr[i][j:j+k]
            if scope == scope[::-1]:
                lst.append(scope)
    
    # 세로 
    for j in range(n):
        for i in range(n-k+1):
            scope = []
            for l in range(k):
                scope.append(arr[i+l][j])
            if scope == scope[::-1]:
                lst.append(scope)
    return lst


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {palin2()}')