from collections import deque

# 한번의 해킹으로 몇대의 컴퓨터를 감염시킬 수 있는가
def bfs(start):
    # 시작점 방문 처리 
    queue = deque()
    queue.append(start)
    visited = [0] * (n+1)
    visited[start] = 1
    cnt = 1

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)
                cnt += 1
    return cnt

# 가장 많은 컴퓨터를 해킹할 수 있는 노드를 찾기
def most_hacking():
    max_hack = 0
    result = []

    for i in range(1, n+1): # i번 컴퓨터를 해킹했을 때 감염되는 개수
        hacking_computers = bfs(i)
        if hacking_computers > max_hack:
            max_hack = hacking_computers
            # result.append(i)
            result = [i] # 더많은걸 찾으면 i로 초기화
        elif hacking_computers == max_hack:  # 같은 수라면 리스트에 추가
            result.append(i)
    return sorted(result)

n, m = list(map(int, input().split()))
graph = [[] for _ in range(n+1)] # 1번부터
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[b].append(a) # b해킹하면 a도 해킹 가능

final = most_hacking()
print(*final)