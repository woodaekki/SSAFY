def cabbage():
    visited = []


T = int(input())
v, e = list(map(int, input().split()))  # 노드 개수, 간선 수
ad_lst = [[] for _ in range(v+1)]
graph = []
for t in range(1, T+1):
    for _ in range(e):
        start, end = list(map(int, input().split()))

        ad_lst[start].append(end)
        ad_lst[end].append(start)
    print(f'#{t} {cabbage()}')