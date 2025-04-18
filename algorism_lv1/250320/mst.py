import sys
sys.stdin = open("mst.txt", "r")

# 대표자 검색 (for 사이클 생성되는지 확인)
def find_set(parents, x):
    # print(parents)
    # 부모가 같으면
    if parents[x] == x:
        return parents[x]

    # 부모가 같지 않으면
    if parents[x] != x:  # 다르면 같을 때까지 부모를 찾기위해 위로 올라감
        parents[x] = find_set(parents, parents[x])
        # print(f"{x}의 부모: {parents[x]}")
        return parents[x]

def union_set(parents, x, y):
    ref_x = find_set(parents, x)
    ref_y = find_set(parents, y)

    # 대표자가 같으면 (사이클 방지)
    if ref_x == ref_y:
        return

    # 대표자 크기가 작은쪽으로 통일
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())
for t in range(1, T+1):
    V, E = list(map(int, input().split())) # 정점 수, 간선 수
    edges = [] # 1. 연결 정보 저장
    for _ in range(E):
        start, end, weight = map(int, input().split()) # 연결된 노드 정보, 가중치
        edges.append((start, end, weight))
    edges.sort(key=lambda x:x[2]) # 2. 가중치 기준으로 오름차순 정렬
    # print(edges)
    parents = [i for i in range(V+1)]

    # u, v가 연결되어 있지 않다면(대표자가 다르다면) 선택
    cnt = 0 # 간선 개수 n-1 지켜야 함
    min_weight = 0 # 최소 비용 저장
    """
    오류 원인: 위의 변수와 이름이 겹침 !!!
    """
    for u, v, w in edges:
        if find_set(parents, u) != find_set(parents, v):
            # 대표자가 다르다면 즉, 다른 집합이라면 연결
            union_set(parents, u, v)
            cnt += 1
            min_weight += w # 가중치합 누적

            if cnt == V:  # 최소 신장 트리 완성
                break

    print(f'#{t} {min_weight}')




