def gualho(arr):
    stack = []
    for i in range(len(arr)):
        if arr[i] == '{' or arr[i] == '(':
            stack.append(arr[i])  
        elif arr[i] == '}' or arr[i] == ')':
            # 스택이 비어있는지 먼저 확인
            if not stack:
                return 0
            if arr[i] == '}' and stack[-1] == '{':
                stack.pop()
            elif arr[i] == ')' and stack[-1] == '(':
                stack.pop()
            else: # (}, {), 등의 경우
                return 0
    
    if stack:
        return 0
    else:
        return 1         

T = int(input())
for t in range(1, T+1):
    arr = list(input())
    print(f'#{t} {gualho(arr)}')

