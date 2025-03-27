import sys
sys.stdin = open("1.txt", "r")

def find_set(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find_set(parents[x])
        return parents[x]


def union_set(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x > ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = [i for i in range(n + 1)]  # 1번부터 시작
    for i in range(0, len(arr), 2):
        union_set(arr[i], arr[i + 1])

    groups = set()
    for i in range(1, n + 1):
        groups.add(find_set(i))
    # print(f"{parents}")
    print(f"#{t} {len(groups)}")
