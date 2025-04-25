import sys
sys.stdin = open('1.txt', "r")

import math 

def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
        return parents[x]
    
    else:
        return parents[x]

def union_set(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return 
    else:
        if ref_x > ref_y:
            parents[ref_y] = ref_x
        else:
            parents[ref_x] = ref_y


n = int(input())
arr = [list(map(float, input().split())) for _ in range(n)]
# print(arr)
parents = [i for i in range(n)]

edges = []
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = arr[i]
        x2, y2 = arr[j]
        star = (x1 - x2)**2 + (y1 - y2)**2
        # 제곱근 계산 방법
        dist = math.sqrt(star)
        edges.append((dist, i, j))

# 크루스칼 가중치 작은 간선 부터 정렬 !
edges.sort(key = lambda x: x[0])
total = 0
for cost, a, b in edges:
    if find_set(a) != find_set(b):
        union_set(a, b)
        total += cost

# 소수점 둘째자리 까지
print(f'{total:.2f}')