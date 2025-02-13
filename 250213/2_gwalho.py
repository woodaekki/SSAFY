txt = input()

top = -1
stack = [0] * 100

ans = 1 # 짝이 맞다고 가정
for x in txt:
    if x == '(': # 여는 괄호면 push
        top += 1
        stack[top] = x

    elif x == ')': # 닫는 괄호인 경우
        if top == -1: # 스택이 비어있는 경우
            ans = 0
            break # 짝이 맞지 않음
        else:
            top -= 1

# 결과적으로 스택이 비어있지 않으면, 짝이 안맞는 것
if top > -1:
    ans = 0

print(ans)


