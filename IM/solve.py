import sys
sys.stdin = open("input.txt", 'r')

def ball():
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]


    for j in range(n-1, -1, -1):
        for i in range(1):


T = int(input())
for t in range(1, T+1):
    n = int(input()) # n x n 배열
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{t} {ball()}')

1. 80의 상하좌우 중 작은 것
lst.append()
lst = [21, 23]

2. 23의 상하좌우 중 작은 것 x
lst.pop()
lst = [21]

3. 21의 상하좌우 중 작은 것 x
lst.pop()
lst = []

4. 그다음 j인 23의 상하좌우 중 작은 것  x