import sys
sys.stdin = open("group.txt", "r")

def find_set(parents, x):
    # print(f"find_set({x}) 호츌")
    if parents[x] == x:  # 부모랑 자기자신이랑 같으면 암거나 반환
        return parents[x]

    if parents[x] != x: # 다르면 같을 때까지 부모를 찾기위해 위로 올라감
        parents[x] = find_set(parents, parents[x])
        # print(f"{x}의 부모: {parents[x]}")
        return parents[x]

def union_set(parents, rank, x, y):
    root_x = find_set(parents, x)
    root_y = find_set(parents, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parents[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parents[root_x] = root_y
        else:
            parents[root_y] = root_x
            rank[root_x] += 1

    # union 끝난 후
    # print(f"union_set({x},{y}): parents: {parents}/ rank: {rank}")

T = int(input())
for t in range(1, T + 1):
    n, m = list(map(int, input().split()))  # 조원 수, 신청서 수
    arr = list(map(int, input().split()))
    parents = [i for i in range(n + 1)]  # 각 원소의 부모를 자신으로 초기화
    rank = [0] * (n + 1)

    for i in range(0, len(arr), 2):
        union_set(parents, rank, arr[i], arr[i + 1])

    # 오류 원인: 부모가 아닌, 대표자의 개수를 세야지 !
    # print(parents)
    # parents = set(parents)
    # cnt = 0
    # for _ in range(1, len(parents)):
    #     cnt += 1
    # print(f'#{t} {cnt}')

    # 각 조원의 대표자 개수 세기
    representative = set(find_set(parents, i) for i in range(1, n + 1))
    cnt = 0
    for _ in representative:
        cnt += 1
    print(f'#{t} {cnt}')