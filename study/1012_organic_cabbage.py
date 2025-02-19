def cabbage():
    n, m, k = list(map(int, input().split())) # 가로, 세로, 배추 개수
    arr = []
    for _ in range(k):
        cabbage = list(map(int, input().split()))
        arr.append(cabbage)

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {cabbage()}')