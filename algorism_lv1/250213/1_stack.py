# 마지막에 삽입한 자료를 가장 먼저 꺼냄 (후입선출)
# 스택에서 마지막 삽입된 원소의 위치를 top 이라고 부름

# 삽입은 push, 삭제는 pop 이라고 부른다
# .isEmpty 는 공백인지 아닌지 확인하는 연산
# .peek 은 top 에 있는 원소를 반환하는 연산

def push(value):
    global top
    top += 1
    stack[top] = value

def pop():
    global top
    value = stack[top]
    top -= 1
    return stack[top]

def is_full():
    return top == size -1

def is_empty():
    # if top == -1:
    #     return True
    # else:
    #     return False
    return top == -1

def peek():
    return stack[top]

size = 10
stack = [-1] * size
top = -1

push(3)
print(top, stack)

push(4)
print(top, stack)

push(10)
print(top, stack)
print(pop())

a = pop()
print(a)
print(top, stack)

print(pop())
print(top, stack)