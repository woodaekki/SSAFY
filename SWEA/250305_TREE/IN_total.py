def calcu(node):
    if type(value[node]) == int:
        return int(value[node])
     
    a = calcu(left[node])
    b = calcu(right[node])
 
    if type(value[node]) == str:
        if value[node] == '+':
            return a + b
        elif value[node] == '-':
            return a - b
        elif value[node] == '*':
            return a * b
        elif value[node] == '/':
            return a / b
 
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
         
        elif len(arr) == 2:
            parent = int(arr[0])
            parent_value = int(arr[1])
            left_child = 0
            right_child = 0
 
            value[parent] = parent_value
            left[parent] = left_child
            right[parent] = right_child
     
    # print(value)
    result = calcu(1)
    print(f'#{t} {int(result)}')