import sys
sys.stdin = open("heap.txt", "r")

def enque(n):
    while n > 1:
        parent = n // 2  
        if tree[parent] > tree[n]: 
            tree[parent], tree[n] = tree[n], tree[parent]
        n = parent  # 부모 노드로 이동

T = int(input()) 
for t in range(1, T + 1):
    n = int(input())  
    numbers = list(map(int, input().split())) 

    tree = [0] * (n + 1)  
    # 힙에 숫자 삽입
    for i in range(n):
        tree[i + 1] = numbers[i]  
        enque(i + 1)  # 삽입 후 최소 힙 유지

    # 마지막 노드의 부모부터 시작해서 조상 노드들의 합 구하기
    root_sum = 0
    node = n // 2  # 마지막 노드의 부모부터 시작
    while node > 0:
        root_sum += tree[node]  # 부모의 값 더하기
        node //= 2  # 부모로 이동
    
    print(f"#{t} {root_sum}")  

    

        

