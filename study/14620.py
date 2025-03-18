import sys
sys.stdin = open("flower.txt", "r")
from itertools import combinations

def check(idx):
    area = set() # 꽃잎의 인덱스가 겹치지 않고 피는지 확인 위함
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 각 꽃잎이 폈을때 상하좌우 네 방향이 겹치는지 체크
    for x, y in idx:
        area.add((x, y))
        for di, dj in directions:
            area.add((x+di, y+dj))
    return area

def flower(n, arr):
    min_cost = float("inf")

    # 꽃잎의 중심이 될 수 있는 구간의 모든 조합 구하기
    center = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            center.append((i,j))
            # print(center)
    combi = list(combinations(center, 3))
    # print(combi)
    for idx in combi:
        blossom = check(idx)
        # 꽃잎이 겹치지 않고 폈다면 15개일 것이므로 길이 확인
        if len(blossom) == 15:
            cost = 0
            for x, y in blossom:
                cost += arr[x][y]
            min_cost = min(min_cost, cost)
    return min_cost

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = flower(n, arr)
print(result)