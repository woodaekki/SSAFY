def calcu2(arr):
    stack = []
    calc = []
    priority = {'+':1, '-':1, '*':2, '/': 2}
 
    # 후위 표기식으로 변환 (전부 str형태)
    for ar in arr:
        if ar.isdigit():
            calc.append(ar)
        else:
            while stack and priority[stack[-1]] > priority[ar]:
                t = stack.pop()
                calc.append(t)
            stack.append(ar)
 
    while stack:
        calc.append(stack.pop())
    # return calc
 
    # 계산 부분분
    nums = []
    for num in calc:
        if num.isdigit():
            nums.append(int(num))
        else:
            b = nums.pop()
            a = nums.pop()
            if num == '+':
                nums.append(a+b)
            elif num == '*':
                nums.append(a*b)
    return nums[0]
     
 
T = 10
for t in range(1, T + 1):
    n = int(input())  
    arr = list(input())  
    result = calcu2(arr)  
    print(f'#{t} {result}')