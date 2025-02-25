import sys
sys.stdin = open("forth.txt", "r")

def forth(arr):
    stack = []
    for i in range(len(arr)):
        if arr[i].isdigit():
            stack.append(int(arr[i]))
        elif arr[i] == '+':
            # 연산자 꺼낼때 스택에 저장된 숫자가 2개미만이면 에러 출력
            if len(stack) < 2:
                return 'error'
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)

        elif arr[i] == '-':
            # 연산자 꺼낼때 스택에 저장된 숫자가 2개미만이면 에러 출력
            if len(stack) < 2:
                return 'error'
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)

        elif arr[i] == '*':
            if len(stack) < 2:
                return 'error'
            c = stack.pop()
            d = stack.pop()
            stack.append(d*c)

        elif arr[i] == '/':
            if len(stack) < 2:
                return 'error'
            c = stack.pop()
            d = stack.pop()
            if c == 0:
                return 'error'
            stack.append(d//c)

        elif arr[i] == '.':
            # 스택에 남은데 .이외 다른게 있으면 에러 출력
            if len(stack) != 1:
                return 'error'
            return stack.pop()
        else:
            # 숫자, 연산자 2개, .이 아니면 에러 출력
            return 'error'
    return 'error'

T = int(input())
for t in range(1, T+1):
    arr = list(map(str, input().split()))
    result = forth(arr)
    print(f'#{t} {result}')