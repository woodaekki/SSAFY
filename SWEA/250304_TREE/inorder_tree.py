def inorder(node):
    if node == 0:
        return
     
    inorder(left[node])
    read.append(value[node])
    inorder(right[node])
    return "".join(read)
 
T = 10
for t in range(1, T+1):
    n = int(input())
 
    left = [0] * (n+1)
    right = [0] * (n+1)
    value = [0] * (n+1)
    for _ in range(n):
        arr = list(map(str, input().split()))
 
        if len(arr) == 4:
            parent = int(arr[0])
            parent_value = arr[1]
            left_child = int(arr[2])
            right_child = int(arr[3])
 
            value[parent] = parent_value
            left[parent] = left_child
            right[parent] = right_child
 
        elif len(arr) == 3:
            parent = int(arr[0])
            parent_value = arr[1]
            left_child = int(arr[2])
            right_child = 0
 
            value[parent] = parent_value
            left[parent] = left_child
            right[parent] = right_child
         
        elif len(arr) == 2:
            parent = int(arr[0])
            parent_value = arr[1]
            left_child = 0
            right_child = 0
 
            value[parent] = parent_value
            left[parent] = left_child
            right[parent] = right_child
     
    # print(value)
    read = []
    result = inorder(1)
    print(f'#{t} {result}')