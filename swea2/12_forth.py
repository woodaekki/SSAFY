import sys
sys.stdin = open("forth.txt", "r")

def forth():
    arr = list(map(str, input().split()))
    num_lst = [] # 숫자만
    mix_lst = [] # 숫자-> 연산자

    # 후위표기법(숫자 -> 연산자)으로 변환
    for i in arr:
        if i.isdigit():
            mix_lst.append(int(i))
            num_lst.append(int(i))
    for j in arr:
        if j == '+' or j == '-' or j == '*' or j == '/' or j == '.':
            mix_lst.append(j)

    for k in range(len(arr)):
        if mix_lst[k] == '+' or mix_lst[k] == '-' or mix_lst[k] == '*' or mix_lst[k] == '/' or mix_lst[k] == '.':
            a = num_lst.pop()
            b = num_lst.pop()
            num_lst.append(a+b)
    return num_lst

T = int(input())
for t in range(1, T+1):
    result = forth()
    print(f'#{t} {result}')
