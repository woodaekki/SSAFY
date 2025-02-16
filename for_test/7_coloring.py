import sys
sys.stdin = open("coloring.txt", "r")

def coloring():
    new = [[0]*10 for _ in range(10)]
    cnt = 0
    n = int(input())
    for _ in range(n):
        row1, col1, row2, col2, color = list(map(int,input().split()))
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                new[i][j] += color
                
    for k in range(10):
        for l in range(10):
            if new[k][l] == 3:
                cnt += 1
    return cnt
        
    
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {coloring()}')