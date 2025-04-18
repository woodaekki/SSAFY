import sys
sys.stdin = open("four.txt", "r")

def order(node):
    if type(cal[node]) == int: # 숫자이면, 숫자 그대로
        return cal[node]
    
    a = order(left[node])
    b = order(right[node])

    if type(arr[1]) == str:
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
    cal = [0]*(n+1)
    left = [0]*(n+1)
    right = [0]*(n+1)
    for _ in range(n):
        arr = list(map(str, input().split()))
        if len(arr) == 4:
            parent = int(arr[0])
            parent_value = arr[1]
            left_child = int(arr[2])
            right_child = int(arr[3])

            cal[parent] = parent_value
            left[parent] = left_child
            right[parent] = right_child
        if len(arr) == 2:
            parent = int(arr[0])
            parent_value = int(arr[1])

            cal[parent] = parent_value
            left[parent] = 0
            right[parent] = 0

    result = order(1)
    print(f'#{t} {int(result)}')