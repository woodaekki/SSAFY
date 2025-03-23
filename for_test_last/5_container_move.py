import sys
sys.stdin = open("1.txt", "r")

def solve():
    container_idx = 0
    truck_idx = 0
    total = 0
    while container_idx < n and truck_idx < m:
        if container[container_idx] <= truck[truck_idx]:
            total += container[container_idx]
            container_idx += 1
            truck_idx += 1
        else:
            container_idx += 1
    return total

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split())) # 컨테이너 수, 트럭 수
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container = sorted(container, reverse=True)
    truck = sorted(truck, reverse=True)
    result = solve()
    print(f'#{t} {result}')