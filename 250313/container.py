import sys
sys.stdin = open("container.txt", "r")

def solve(n,m, container, truck):
    load = []
    container_idx = 0
    truck_idx = 0
    while container_idx < n and truck_idx < m:
        if truck[truck_idx] >= container[container_idx]:
            load.append(container[container_idx])
            truck_idx += 1
            container_idx += 1
        else:
            container_idx += 1
                
    return sum(load)

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split())) # 컨테이너 수 / 트럭 수
    container = list(map(int, input().split())) # 화물의 무게 # 5 3 1
    truck = list(map(int, input().split())) # 트럭의 적재용량 # 8 3
    container = sorted(container, reverse=True)
    truck = sorted(truck, reverse=True)
    result = solve(n,m, container, truck)
    print(f'#{t} {result}')