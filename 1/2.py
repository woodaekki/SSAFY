import heapq

def prim(root): # 시작 지점을 0으로 잡고
    pq = []
    heapq.heappush(pq, (0,root)) # 거리, 시작지점 을 pq에 튜플로 할당
    MST = [0] * (N+1) # visited 역할을 할 MST할당하고
    min_dist = 0 # 최소 거리를 할당하기위한 변수

    while pq: # pq가 없으면 종료
        dist, node = heapq.heappop(pq) # dist와 node를 heapq 팝을 할당 한다.

        if MST[node]: #만약 그 지점이 0이 아니면
            continue #넘긴다

        MST[node] = 1 # 0이면 1을 집어넣고
        min_dist += dist # 최소 거리에 현재 거리만큼을 더한다

        for next_node in range(len(graph)): # 그래프의 크기만큼 돌리고
            if MST[next_node]: # 다음 노드가 간적이 있으면
                continue # 넘긴다

            heapq.heappush(pq,(graph[node][next_node],next_node))
            # 그렇지않으면 heapqpush로 pq에 node에서 출발하여 next_node에 도착하는 지점의 길이와 다음 지점의 인덱스를 푸쉬해준다.

    return min_dist #최소값 리턴


T = int(input()) # 테스트 케이스만큼 할당
for case in range(1, T+1): # T 만큼 케이스를 돌리고
    N = int(input()) # 콘센트의 개수를 받고
    con = [(0,0)] # 누전차단기는 0,0 이므로 할당
    graph = [[0] * (N+1) for _ in range(N+1)] # 콘센트 + 누전차단기이므로 N+1

    for _ in range(N): # 콘센트만큼 돌린다
        x, y = map(int,input().split()) # x, y 좌표를 할당받고
        con.append((x,y)) # con에 추가해준다.


    for i in range(N+1): # con의 크기만큼 포문
        for j in range(N+1): # con의 크기만큼 포문
            graph[i][j] = abs(con[i][0] - con[j][0]) + abs(con[i][1] - con[j][1]) # i에서 j까지의 거리를 잰다.
    print(graph)
    result = prim(0) #result에 prim 결과값 할당
    print(f'#{case} {result}')