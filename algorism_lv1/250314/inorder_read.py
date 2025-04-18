import sys
sys.stdin = open("reading.txt", "r")

def inorder(node):
    if node == 0:
        return

    inorder(left[node])
    read.append(value[node])
    inorder(right[node])
    return "".join(read)

T = 10
for t in range(1, T+1):
    n = int(input()) # 정점 수
    left = [0] * (n+1)
    right = [0] * (n+1)
    value = [0] * (n+1)
    read = []
    for _ in range(n):
        arr = list(map(str, input().split()))
        # p, p_val, l, r
        if len(arr) == 4:
            p = int(arr[0])
            p_val = arr[1]
            l = int(arr[2])
            r = int(arr[3])
            value[p] = p_val
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

    result = inorder(1)
    print(f'#{t} {result}')
