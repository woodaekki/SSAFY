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
    v, e = list(map(int, input().split()))
    edges = []
    parents = [i for i in range(v+1)]
    for _ in range(e):
        a, b, c = list(map(int, input().split()))
        edges.append((a, b, c))
    edges.sort(key=lambda x: x[2])
    # print(edges)
    cnt = total = 0
    for a, b, c in edges:
        if find_set(a) != find_set(b):
            union_set(a, b)
            total += c
            cnt += 1
        if cnt == v-1:
            break
    print(f'#{t} {total}')