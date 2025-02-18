import sys
sys.stdin = open("forth.txt", "r")

def forth():
    arr = list(map(str, input().split()))  
    num_lst = []  # 숫자만 
    mix_lst = []  # 숫자-> 연산자

    for i in arr:
        # 후위표기법으로 변환
        if i.isdigit():  
            num_lst.append(int(i))  
            mix_lst.append(int(i))  
        elif i == '+' or i == '-' or i == '*' or i == '/':  
            mix_lst.append(i)
  
            if len(num_lst) < 2: 
                return 'error'
            b = num_lst.pop()  
            a = num_lst.pop()

            # 마지막 2개 빼서 계산하고 다시 넣기
            if i == '+':
                num_lst.append(a + b)
            elif i == '-':
                num_lst.append(a - b)
            elif i == '*':
                num_lst.append(a * b)
            elif i == '/':
                if b == 0: #zerodivisionerror 막기 !
                    return 'error'
                num_lst.append(a // b) 
        elif i == '.':  
            if len(num_lst) != 1: # 마지막에 . 이외에 다른게 남으면 에러 
                return 'error'
    return num_lst

T = int(input())  
for t in range(1, T + 1):
    result = forth()
    if result == 'error': # e만 출력되는 거 막기 
        print(f'#{t} error') 
    else:
        print(f'#{t} {result[0]}')
