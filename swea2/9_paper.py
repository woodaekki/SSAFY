import sys
sys.stdin = open("road.txt", "r")

def search_road(start, end):
    visited = [False] * 100 #  방문 노드 저장 리스트
    stack = []
    visited[start] = True # 첫번째 노드 방문
    stack.append(start)

    while stack: # 스택이 차있으면
        node = stack.pop() # 가장 마지막에 들어간 노드를 뽑아서
        if node == end: # 그 노드가 종점 노드이면 길이 연결된 것이므로 1 반환
           return 1

        for k in graph[node]:
            if not visited[k]:
                visited[k] = True
                stack.append(k)
    return 0 # 스택에서 다 꺼냈는데 연결할 노드가 없으면 0 반환

T = 10
start, end = 0, 99 # 출발도시 A, 도착도시 B
for t in range(1, T+1):
    tc, n = map(int, input().split()) # 테스트 케이스 번호, 간선 수
    graph = [[] for _ in range(100)] # [[], [o, o], [o, o], ...] / 총 100개 저장할 리스트
    road = list(map(int, input().split())) # o -> o로 가는 정보 리스트 저장

    for i in range(n):
        graph[road[2*i]].append(road[2*i+1]) # 단방향 그래프

    print(f'#{t} {search_road(start, end)}')