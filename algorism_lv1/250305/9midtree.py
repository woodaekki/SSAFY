import sys
sys.stdin = open("9midtree.txt", "r")

def midtree(node):
    # 왼쪽이나 오른쪽이 없을 경우
    if type(cal[node]) == int:  # cal[node]가 숫자일 경우
        return cal[node] # 그 숫자 그대로 

    # 왼쪽, 부모, 오른쪽 순으로 호출
    a = midtree(left[node])
    b = midtree(right[node])
    
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
    n = int(input()) # 노드 수
    left = [0] * (n+1)
    right = [0] * (n+1)
    cal = [0] * (n+1)
    for _ in range(n):
        arr = list(map(str, input().split())) # 루트,연산자,왼쪽,오른쪽
        root = int(arr[0])
        # 연산자이면 
        if arr[1] == '+' or arr[1] == '-' or arr[1] == '*' or arr[1] == '/':
            cal[root] = arr[1]
            left[root] = int(arr[2])
            right[root] = int(arr[3])
        else:
            cal[root] = int(arr[1])       
    # print(left,right,cal)
    result = midtree(1) # 1번 노드부터 계산 
    print(f'#{t} {int(result)}') # 소수점 버림 처리 


