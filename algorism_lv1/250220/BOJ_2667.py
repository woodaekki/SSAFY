import sys
sys.stdin = open("2178.txt", "r")

from collections import deque

def bfs(x, y):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 시작점 방문 처리
    queue = deque()
    queue.append((x,y))
    visited[x][y] = cnt
    house = 1 # 시작점 방문처리했으니 집의 수는 1개

    while queue:
        x, y = queue.popleft() # 선입된걸 빼서
        for di, dj in directions:
            ni, nj = x+di, y+dj
            # 경계 안에 있는데, 1인데 방문하지 않았으면
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 and not visited[ni][nj]:
                # 방문하고 큐에 넣는다
                visited[ni][nj] = cnt
                house += 1
                queue.append((ni, nj))
    return house


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
# print(arr)
visited = [[0] * n for _ in range(n)] # 새로운 방문목록 만들기
house_lst = []
cnt = 1 # 단지 수
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]: # 전체 순회를 돌면서 1인데, 방문하지 않았으면
            house_lst.append(bfs(i, j)) # bfs함수를 불러 상하좌우로 끊길 때까지 쭉 1을 따라가기
            cnt += 1 # 부를때마다 카운트 1증가

print(cnt-1) # 단지 카운트를 1부터 시작했으니까
sorted_house = sorted(house_lst)
for home in sorted_house:
    print(home)