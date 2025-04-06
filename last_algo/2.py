def find_set(x):
    if parents[x] == x:
        return parents[x]
    else:
        parents[x] = find_set(parents[x])
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

T = int(input())
for t in range(1, T+1):
    V, E = list(map(int, input().split()))
    parents = [i for i in range(V+1)]
    edges = []
    for _ in range(E):
        n1, n2, weight = list(map(int, input().split()))
        edges.append((n1, n2, weight))
    edges.sort(key=lambda x:x[2])
    cnt = total = 0
    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union_set(u, v)
            cnt += 1
            total += w
        if cnt == V:
            break
    print(f'#{t} {total}')