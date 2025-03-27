# 유니언 파인드에서 사이클이 발생하는 경우
# 같은 루트를 가진 정점 2개를 연결하려 할때
import sys
sys.stdin = open("1.txt", "r")

def find_set(x):
    # 부모가 같으면
    if parents[x] == x:
        return parents[x]
    else:
        parents[x] = find_set(parents[x])
        return parents[x]

def union_set(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 대표자가 같으면 (사이클 방지)
    if ref_x == ref_y:
        return

    if ref_x > ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())
for t in range(1, T+1):
    v, e = list(map(int, input().split()))
    edges = []
    for _ in range(e):
        n1, n2, weight = map(int, input().split())
        edges.append((n1, n2, weight))
    edges.sort(key=lambda x:x[2])
    parents = [i for i in range(v+1)]

    cnt = 0
    min_weight = 0
    for i, j, w in edges:
        if find_set(i) != find_set(j):
            # 대표자가 다르다면 즉, 다른 집합이라면 연결
            union_set(i, j)
            cnt += 1
            min_weight += w

            if cnt == v:
                break
    print(f'#{t} {min_weight}')
