from collections import deque

def virus(start, end):
    visited = [0] * (n+1) # 1번부터 출발, 방문 목록 저장
    cnt = 0

    # 큐 생성 및 시작노드 방문 처리
    queue = deque()
    queue.append(start)
    visited[start] = 1

    # 큐 안에 노드가 남아있을 동안 순회
    while queue:
        # 선입된 노드 빼서
        t = queue.popleft()
        # 뺀 노드의 인접노드에서 방문하지 않은 노드가 있다면
        for w in adj_l[t]:
            if visited[w] == 0:
                visited[w] = 1
                queue.append(w)  # 큐에 넣기
                cnt += 1
    return cnt


n = int(input()) # 노드 수
m = int(input()) # 간선 수
adj_l = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = list(map(int, input().split()))
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

result = virus(1, n)
print(result)