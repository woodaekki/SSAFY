import sys
sys.stdin = open("maze.txt", "r")

# 0은 구멍, 1은 벽, 2는 출발, 3은 도착
# 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지

def bfs(i, j, n):  # 시작위치 i, j / 크기 n
    visited = [[0] * n for _ in range(n)]
    queue = []
    queue.append([i, j])  # 시작점 큐에 넣고
    visited[i][j] = 1  # 방문 처리

    # 큐가 비워질 때까지 반복
    while queue:
        ti, tj = queue.pop(0)
        if maze[ti][tj] == 3:  # 도착지에 도착하면
            return visited[ti][tj] - 2  # 출발부터 도착까지의 칸 수

        # t에 인접 w중, 방문하지 않은 곳이 있다면
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            wi, wj = ti + di, tj + dj
            # 경계에서 벗어나지 않은 상태에서, 벽이 아닌데, 방문하지 않았다면
            if 0 <= wi < n and 0 <= wj < n and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                queue.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1  # 방문 처리
    return 0  # 도착하지 못하면 0 반환

def find_start(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j

T = int(input())  # 테스트 케이스 수
for t in range(1, T + 1):
    n = int(input())  # n x n 배열 크기
    maze = [list(map(int, input())) for _ in range(n)]

    start, end = find_start(n)  # 출발 위치 찾기
    result = bfs(start, end, n)  # BFS로 최단 경로 계산

    print(f'#{t} {result}')
