import sys
sys.stdin = open("3.txt", "r")

def bus(typed, a, b, visited):
    # 출발과 종점은 무조건 방문
    if typed == 1:
        for i in range(a, b+1):
            if visited[i] == 0:
                visited[i] += 1
        # print(visited)
    elif typed == 2:
        if a % 2 == 0:
            for i in range(a, b+1, 2):
                visited[i] += 1
        else:
            for j in range(a, b+1, 2):
                visited[j] += 1

        # # 출발점과 종점은 무조건 방문
        # visited[a] += 1
        # visited[b] += 1
        # print(visited)

    elif typed == 3:
        if a % 2 == 0:
            for i in range(a, b+1):
                if i % 4 == 0:
                    visited[i] += 1
        else:
            for j in range(a, b+1):
                if j % 3 == 0 and j % 10 != 0:
                    visited[j] += 1

    # 출발점과 종점은 무조건 방문


    # 몇개의 노선이 같은 정류장에 정차하는지


T = int(input())
for t in range(1, T+1):
    n = int(input())
    visited = [0] * 15
    for _ in range(n):
        typed, a, b = map(int, input().split()) # 버스타입(1:일반,2:급행,3:광역)/출발/ 종점
        result = bus(typed, a, b, visited)
    print(f'#{t} {result}')