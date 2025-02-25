import sys
sys.stdin = open("calcu.txt", "r")

def calcu2(arr):
    # 스택(연산자의 우선순위를 구분하기 위함)
    stack = []
    # 후위 표기식 
    calc = []
    
    # 연산자 우선순위 딕셔너리
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    for ar in arr:
        # 숫자인 경우
        if ar.isdigit():
            calc.append(ar)
        # 연산자인 경우
        else:
            # 스택에서 우선순위가 더 높은 연산자가 나올 때까지 pop해서 출력
            while stack and priority[stack[-1]] > priority[ar]:
                t = stack.pop()
                calc.append(t)
            stack.append(ar)
    
    # 남은 연산자 있으면 마저 넣기
    while stack:
        calc.append(stack.pop())
    
    # 계산 부분 
    nums = []
    for num in calc:
        if num.isdigit():
            nums.append(int(num))
        else:
            b = nums.pop()
            a = nums.pop()
            if num == '+':
                nums.append(a + b)
            elif num == '*':
                nums.append(a * b)
    
    return nums[0]

T = 10
for t in range(1, T + 1):
    n = int(input())  
    arr = list(input())  
    result = calcu2(arr)  
    print(f'#{t} {result}')


