def dfs(start, end):
    visited = [0] * (n+1) # 방문 목록 저장
    # 시작점 저장
    stack = []
    stack.append(r)
    visited[r] = 1

    while stack:
        t = stack.pop(-1)
        print(t)
        for w in adj_l[t]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(w)
    return 0 # 도달할 수 없으면 0 반환


n, m, r = list(map(int, input().split()))  # 정점의 수, 간선의 수, 시작 정점
adj_l = [[] for _ in range(n+1)]  # 인접 리스트 초기화

# 간선 입력 받기
for _ in range(m):
    v1, v2 = list(map(int, input().split()))
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

result = dfs(r, n)
print(result)


