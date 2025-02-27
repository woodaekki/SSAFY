import sys
sys.stdin = open("pizza.txt", "r")

def pizza():
    oven = [0] * n # 화덕 생성
    waiting_pizza = n+1 # 대기중인 피자

    # 화덕의 길이만큼 피자를 넣는다.
    for i in range(1, n+1):
        pizza_idx = i
        oven[i-1] = pizza_idx, cheezes[i]
        # print(oven)
    
    # 치즈를 다 쓸때까지 반복한다. 
    while len(oven) > 1:
        pizza_index, cheeze = oven.pop(0)
        # 화덕의 길이만큼 치즈를 빼내 반으로 줄인다.
        cheeze = cheeze // 2
        oven.append(cheeze)
        # 치즈가 다 녹으면 화덕에서 꺼내고, 대기중인 다음 피자를 넣는다.
        if cheeze <= 0:
            oven.pop()
            pizza_index = waiting_pizza
    # 마지막 남은 피자 번호 반환
    return pizza_index

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    cheezes = [0] + list(map(int, input().split()))
    result = pizza()
    print(f'#{t} {result}')
