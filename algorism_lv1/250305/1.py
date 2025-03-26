N = 13
s = '1 2 1 3 2 4 2 6 5 6'

TREE = [[0, 0] for _ in range(N+1)]
lst = list(map(int, s.split()))
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    if TREE[p][0]:  #왼쪽에 데이터가 있으면
        TREE[p][1] = c
    else:
        TREE[p][0] = c

print(TREE)

def in_order(T):
    if T:
        in_order(TREE[T][0])
        print(T)
        in_order(TREE[T][1])

in_order(1)
