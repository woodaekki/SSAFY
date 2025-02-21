def chess():
    pass

T = int(input())
for _ in range(T):
    n = int(input())
    before = list(map(int, input().split())) # 현재
    after = list(map(int, input().split())) # 이동하려는 칸

for i in range(n):
    for j in range(n):
        before[i][j] = 0