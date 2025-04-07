
def find_set(x):
    if x == parents[x]:
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
    n, m = list(map(int, input().split()))
    arr= list(map(int, input().split()))
    parents = [i for i in range(n+1)]
    for i in range(0, len(arr), 2):
        union_set(arr[i], arr[i+1])

    group = set()
    for j in range(1, n+1):
        group.add(find_set(j))

    print(f'#{t} {len(group)}')
