# 최대힙

def enq(n):
    global last
    last += 1       # 마지막 정점 공간 확장
    heap[last] = n  # 마지막 정점에 key 추가

    c = last        # 자식노드중 젤 마지막
    p = c // 2      # 완전이진트리에서 부모 정점 번호
    while p!=0 and heap[p] < heap[c]: # 부모가 있고, 부모 < 자식 인경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = heap[1]           # 루트 노드의 원소 저장
    heap[1] = heap[last]    # 삭제할 노드 루트 노드 자리로 이동
    last -= 1               # 삭제한 노드 공간 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2               # 왼쪽 자식
    while c <= last:        # 자식이 하나라도 있으면
        # 힙의 자식 노드에서 왼쪽과 오른쪽 자식의 크기 순서는 상관이 없음
        if c+1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식이 있는데, 오른쪽 자식이 더 크면
            c += 1                      # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:   # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c               # 자식을 새로운 부모로
            c = p * 2           # 왼쪽 자식 번호를 계산
        else:                   # 부모가 더 크면
            break               # 비교 중단,
    return tmp

heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
while last:
    print(deq())