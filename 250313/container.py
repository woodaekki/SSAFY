import sys
sys.stdin = open("container.txt", "r")

def solve():
    pass

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split())) # 컨테이너 수 / 트럭 수
    weight = list(map(int, input().split())) # 화물의 무게
    capacity = list(map(int, input().split())) # 트럭의 적재용량
    result = solve()
    print(f'#{t} {result}')