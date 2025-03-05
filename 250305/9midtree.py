# import sys
# sys.stdin = open("9midtree.txt", "r")

def midtree(T):
    # 왼쪽, 부모, 오른쪽 순으로 호출
    if T:
        midtree(left[T])
        read.append(value[T])
        midtree(right[T])
    return "".join(read)

T = 10
for t in range(1, T+1):
    n = int(input()) # 노드 수
    left = [0] * (n+1)
    right = [0] * (n+1)
    value = [0] * (n+1)
    read = []
    for _ in range(n):
        arr = list(map(str, input().split()))
        # p, p_val, l, r (p, p번에 들어갈 값, p의 왼쪽 자식, p의 오른쪽 자식
        # 완전 이진 트리
        if len(arr) == 4:
            p = int(arr[0])
            p_val = arr[1]
            l = int(arr[2])
            r = int(arr[3])
            value[p]=p_val
            left[p] = l  # 왼쪽 자식 번호 저장
            right[p] = r
        if len(arr) == 3:
            p = int(arr[0])
            p_val = arr[1]
            l = int(arr[2])
            r = 0
            value[p] = p_val
            left[p] = l  # 왼쪽 자식 번호 저장
            right[p] = r
        if len(arr) == 2:
            p = int(arr[0])
            p_val = arr[1]
            l = 0
            r = 0
            value[p] = p_val
            left[p] = l  # 왼쪽 자식 번호 저장
            right[p] = r

    result = midtree(1)
    print(f'#{t} {result}')


