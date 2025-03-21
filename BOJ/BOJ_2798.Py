import sys
sys.stdin = open("net.txt", "r")

# 부모 찾기
def find_set(x):
    # 부모가 같으면
    if parents[x] == x:
        return parents[x]

    # 부모가 다르면
    else:
        parents[x] = find_set(parents[x])
        return parents[x]

# 연결하기
def union_set(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 사이클 방지
    if ref_x == ref_y:
        return

    # 부모가 작은 쪽으로 통합
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

N = int(input())
M = int(input())
edges = []
parents = [i for i in range(N+1)] # 컴퓨터 번호는 1번부터 시작
# print(parents)
for _ in range(M):
    a, b, cost = list(map(int, input().split()))
    edges.append((a, b, cost)) # (a에서 b로 연결, 비용)
# 가중치 기준으로 정렬
edges.sort(key= lambda x:x[2])
# print(edges)

min_cost = cnt = 0
# 연결되어 있지 않으면 연결
for u, v, w in edges:
    if find_set(u) != find_set(v):
        union_set(u,v)
        min_cost += w
        cnt += 1

        if cnt == N - 1: # mst 완성되면 끝
            break
print(min_cost)