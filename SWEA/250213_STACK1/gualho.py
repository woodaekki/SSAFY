def gualho():
    stack = []
    for i in range(n):
        if arr[i] == '(' or arr[i] == '[' or arr[i] == '{' or arr[i] == '<':
            stack.append(arr[i])
         
        elif arr[i] == ')' or arr[i] == ']' or arr[i] == '}' or arr[i] == '>':
            if not stack:
                return 0
             
            elif arr[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif arr[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif arr[i] == '}' and stack[-1] == '{':
                stack.pop()
            elif arr[i] == '>' and stack[-1] == '<':
                stack.pop()
            else: # 생뚱맞은 괄호 조합일 경우
                return 0
     
    if stack:
        return 0
    else:
        return 1
 
T = 10
for t in range(1, T+1):
    n = int(input()) # 문자열의 길이
    arr = list(input())
    print(f'#{t} {gualho()}')