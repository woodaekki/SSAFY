import sys
sys.stdin = open("tree.txt", "r")

def calcu(node):
    if type(cal[node]) == int:
        return int(cal[node])
    
    a = calcu(left[node])
    b = calcu(right[node])

    if type(cal[node]) == str:
        if cal[node] == '+':
            return a + b
        elif cal[node] == '-':
            return a - b
        elif cal[node] == '*':
            return a * b
        elif cal[node] == '/':
            return a / b

T = 10
for t in range(1, T+1):
    n = int(input())

    left = [0]*(n+1)
    right = [0]*(n+1)
    cal = [0]*(n+1)
    for _ in range(n):
        arr = list(map(str, input().split()))
        if len(arr) == 4:
            parent = int(arr[0])
            parent_value = arr[1]
            left_child = int(arr[2])
            right_child = int(arr[3])

            left[parent] = left_child
            right[parent] = right_child
            cal[parent] = parent_value
        
        elif len(arr) == 2:
            parent = int(arr[0])
            parent_value = int(arr[1])
            left_child = 0
            right_child = 0

            left[parent] = left_child
            right[parent] = right_child
            cal[parent] = parent_value
   
    result = calcu(1)
    print(f'#{t} {int(result)}')
