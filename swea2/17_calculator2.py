import sys
sys.stdin = open("calculator2.txt", "r")

def calculator2(s):
    result = []
    stack = []
    isp = {'+':1, '-':1, '*':2, '/':2, '(':0} # 스택 안
    icp = {'+':1, '-':1, '*':2, '/':2, '(':3} # 스택 밖 
 
    for c in s:
        if c.isdigit(): # 피연산자
            result.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop(-1))
            stack.pop(-1)
        else: # 연산자
            if not stack or isp[stack[-1]] < icp[c]:
                stack.append(c)
            else:
                while stack and isp[stack[-1]] >= icp[c]:
                    result.append(stack.pop(-1))
                stack.append(c)
    while stack:
        result.append(stack.pop(-1))
 
    return result
 
def cal(op1, op2, ope):
    if ope == '+':
        return op2 + op1
    if ope == '-':
        return op2 - op1
    if ope == '*':
        return op2 * op1
    if ope == '/':
        return op2 // op1
 
 
def step2(lst):
    stack = []
    for c in lst:
        if c.isdigit():
            stack.append(int(c))
        else:
            value1 = stack.pop(-1)
            value2 = stack.pop(-1)
            stack.append(cal(value1, value2, c))
 
    return stack.pop(-1)
 
for t in range(1, 11):
    N = int(input())
    s = list(input())
 
    post_order = calculator2(s)
    print(f'#{t} {step2(post_order)}')

