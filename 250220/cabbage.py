def cabbage():
    m, n, k = list(map(int, input().split()))
    for _ in range(n):
        j, i = list(map(int, input().split()))

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {cabbage()}')