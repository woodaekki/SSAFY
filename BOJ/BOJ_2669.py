def paper():
    n = int(input())
    new = [[0] * 101 for _ in range(101)]
    for _ in range(n):
        x1, y1 = list(map(int, input().split()))
        for i in range(x1, x1+10):
            for j in range(y1, y1+10):
               new[i][j] = 1
    
    cnt = 0
    for a in range(101):
        for b in range(101):
            if new[a][b] == 1:
                cnt += 1
    return cnt

print(paper())