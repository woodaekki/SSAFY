# 마지막에 삽입한 자료를 가장 먼저 꺼냄 (후입선출)
# 스택에서 마지막 삽입된 원소의 위치를 top 이라고 부름

# 삽입은 push, 삭제는 pop 이라고 부른다
# .isEmpty 는 공백인지 아닌지 확인하는 연산
# .peek 은 top 에 있는 원소를 반환하는 연산

# 간단한 스택 구현
top = -1
stack = [0] * 10

top += 1 # push(1)
stack[top] = 1

top += 1 # push(2)
stack[top] = 2

top += 1 # push(3)
stack[top] = 3

top -= 1 # pop
print(stack[top+1])

top -= 1 # pop
print(stack[top+1])

top -= 1 # pop
print(stack[top+1])