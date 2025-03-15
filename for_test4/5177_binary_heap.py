import sys
sys.stdin = open("tree.txt", "r")

def min_heap_sum():
    heap = []  
    for num in arr:
        heap.append(num)
        idx = len(heap) - 1  # 마지막 노드 인덱스
        
        # 최소힙: 루트에 항상 가장 작은 값이 저장되어야 함 
        while idx > 1 and heap[idx] < heap[idx // 2]: # 부모보다 작으면 교환 
            heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
            idx //= 2  # 부모 노드로 이동

    # 마지막 노드의 조상 노드 값의 합 구하기
    last = len(heap) - 1  
    total = 0
    while last > 1:  # 루트 노드가 될때까지 이동해서 구하기 
        last //= 2
        total += heap[last]

    return total

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f"#{t} {min_heap_sum()}")