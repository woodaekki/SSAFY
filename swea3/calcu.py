import sys
sys.stdin = open("calcu.txt", "r")

def calcu2():
    num_lst = [] # 숫자만
    mix_lst = [] # 숫자 -> 연산자
    for i in range(len(arr)):
        if arr[i].isdigit():
            num_lst.append(int(arr[i]))
            mix_lst.append(arr[i])

        elif arr[i] == '+' or arr[i] == '*':
            mix_lst.append(arr[i])

    for j in range(len(mix_lst)):
        if mix_lst[j] == '+':
            a = num_lst.pop(0)
            b = num_lst.pop(0)
            num_lst.append(b+a)
        elif mix_lst[j] == '*':
            a = num_lst.pop(0)
            b = num_lst.pop(0)
            num_lst.append(b*a)
    return num_lst

T = 1
for t in range(1, T + 1):
    n = int(input())
    arr = list(input())
    result = calcu2()
    print(f'#{t} {result}')

