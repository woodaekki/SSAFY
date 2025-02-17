import sys
sys.stdin = open("calculator.txt", "r")

def calculator():
    n = int(input())
    arr = list(input())
    num_lst = [] # 숫자만
    mix_lst = [] # 숫자-> 연산자

    # 후위표기법(숫자 -> 연산자)으로 변환
    for i in arr:
        if i.isdigit():
            mix_lst.append(i)
            num_lst.append(int(i))
    for j in arr:
        if j == '+':
            mix_lst.append(j)

    for k in range(n):
        if mix_lst[k] == '+':
            a = num_lst.pop()
            b = num_lst.pop()
            num_lst.append(a+b)

    return num_lst

T = 10
for t in range(1, T+1):
    result = calculator()
    print(f'#{t} {result[0]}')

