import sys
sys.stdin = open("graph.txt", "r")

def dfs(start, end):
    visited = [False] * (v + 1)  # 방문 여부 리스트 (1번 노드부터)
    stack = []
    visited[start] = True # 시작 노드 방문
    stack.append(start)

    while stack: # 스택에 데이터가 있는 경우
        node = stack.pop()  # 가장 마지막에 들어간 노드 뽑아내서
        if node == end: # 도착노드와 같으면 끝까지 연결되어있다는 것이므로 1반환
            return 1

        # 간선이 있는 경우
        for k in graph[node]: # 간선 정보가 저장되어있는 리스트에서
            if not visited[k]: # 방문하지 않은 노드가 있다면
                visited[k] = True # 방문하고
                stack.append(k) # 스택에 넣기

    # 다 pop 시킨 후 간선이 없어 더 넣을 노드가 없다는 것은 끊겼다는 것이므로 0 반환
    return 0

T = int(input())
for t in range(1, T + 1):
    v, e = map(int, input().split()) # 노드 수, 간선 수
    graph = [[] for _ in range(v + 1)] # 간선 정보 저장할 리스트 생성

    for _ in range(e):
        S, G = map(int, input().split()) # 간선수만큼 그래프 모양 입력
        graph[S].append(G) # 단방향

    start, end = map(int, input().split()) # 시작노드, 도착 노드

    result = dfs(start, end) # 1번 노드부터 시작
    print(f'#{t} {result}')