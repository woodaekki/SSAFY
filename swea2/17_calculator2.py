import sys
sys.stdin = open("calculator2.txt", "r")

def calculator2():
    n = int(input())
    arr = list(input())

    priority = {'*': 2, "+": 1}
    num_list = [] # 숫자만
    mix_list = [] # 숫자 -> 연산자

    # 후위 표기식으로 변환
    for i in arr:
        if i.isdigit():
            num_list.append(int(i))
            mix_list.append(int(i))

    for j in arr:
        if j == '+' or j == '*':
            mix_list.append(j)

    for k in range(n):
        if mix_list[k] == '+':
            a = num_list.pop()
            b = num_list.pop()
            num_list.append(a+b)

        elif mix_list[k] == '*':
            a = num_list.pop()
            b = num_list.pop()
            num_list.append(a*b)

    return num_list

T = 10
for t in range(1, T+1):
    print(f'#{t} {calculator2()}')