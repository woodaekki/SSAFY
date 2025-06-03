def bus(type, a, b, visited):
    # 무조건 a, b는 방문해야 함
    visited[a] += 1
    visited[b] += 1
 
    if type == 1: 
        for i in range(a+1, b):
            visited[i] += 1
             
    elif type == 2: 
        if a % 2 == 0:
            for i in range(a+2, b, 2):
                visited[i] += 1
        else:
            for i in range(a+2, b, 2):
                visited[i] += 1
 
    elif type == 3:  
        if a % 2 == 0:
            for i in range(a+1, b):
                if i % 4 == 0:
                    visited[i] += 1
        else:
            for i in range(a+1, b):
                if i % 3 == 0 and i % 10 != 0:
                    visited[i] += 1
     
    return max(visited)
 
T = int(input())
for t in range(1, T + 1):
    n = int(input())
    visited = [0] * 1001
    for _ in range(n):
        type, a, b = list(map(int, input().split()))
        bus(type, a, b, visited)
    print(f'#{t} {max(visited)}')