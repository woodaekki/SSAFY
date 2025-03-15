import sys
sys.stdin = open("reading.txt", "r")

def inorder(node):
    if node == 0:
        return
    
    inorder(left[node])
    result.append(value[node])
    inorder(right[node])
    return "".join(result)

T = 10
for t in range(1, T+1):
    n = int(input())
    left = [0] * (n+1)
    right = [0] * (n+1)
    value = [0] * (n+1)
    result = []
    for _ in range(n):
        arr = list(map(str, input().split()))

        if len(arr) == 4:
            parent = int(arr[0])
            parent_val = arr[1]
            left_child = int(arr[2])
            right_child = int(arr[3])
            value[parent] = parent_val
            left[parent] = left_child
            right[parent] = right_child
        if len(arr) == 3:
            parent = int(arr[0])
            parent_val = arr[1]
            left_child = int(arr[2])
            right_child = 0
            value[parent] = parent_val
            left[parent] = left_child
            right[parent] = right_child
        if len(arr) == 2:
            parent = int(arr[0])
            parent_val = arr[1]
            left_child = 0
            right_child = 0
            value[parent] = parent_val
            left[parent] = left_child
            right[parent] = right_child
    
    result = inorder(1)
    print(f'#{t} {result}')
    