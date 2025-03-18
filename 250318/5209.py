import sys
sys.stdin = open("pro.txt", "r")

def product_cost(visited, product, curr_cost):
    global min_cost
    # 1번 잘못된 점: 여기다가 작성하면 매번 무한대를 불러와서 현재비용이랑 비교하니 아래 조건 무의미
    # min_cost = float("inf")
    # 최소 비용 같거나 이미 넘었으면 반환
    if curr_cost >= min_cost:
        return

    if product == n: # 모든 제품 다 봤을때
        # 최저 비용을 갱신
        # 첫번째 예시는 73 - 11 - 24 - 31 - 83에서 갱신
        if curr_cost < min_cost:
            min_cost = curr_cost
        return

    for factory in range(n):
        if visited[factory]:
            continue
        visited[factory] = 1
        product_cost(visited, product+1, curr_cost+arr[product][factory])
        visited[factory] = 0
    return

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_cost = float("inf")
    product_cost(visited, 0, 0)
    print(f'#{t} {min_cost}')