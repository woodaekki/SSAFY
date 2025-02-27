import sys
sys.stdin = open("pizza.txt", "r")

def pizza():
    oven = [0] * (n+1)
    waiting_pizza = m-n

    # 화덕 한바퀴
    # 피자번호는 1번부터 
    for i in range(1, n+1):
        # 피자 인덱스 알아놓기
        pizza_idx = oven.pop(i)
        print(pizza_idx)
        # print(pizza_idx)
        oven.append(pizza_idx) 
        # print(oven)
        # 화덕한바퀴 돌때 치즈량은 절반으로 
        cheeze = arr.pop(i)
        arr.append(cheeze//2)
        # print(arr)
        # 치즈량이 0이하가 되면 화덕에서 꺼내고, 그 자리에 남은 피자 넣기기
        if cheeze <= 0:
            arr.pop(cheeze)
            pizza_idx = waiting_pizza +1
    return pizza_idx

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = pizza()
    print(f'{result}')
