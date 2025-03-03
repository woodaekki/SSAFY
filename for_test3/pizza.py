import sys
sys.stdin = open("pizza.txt","r")

def pizza(n,m,cheezes):
    oven = []
    waiting_pizza = n+1

    # 오븐에 피자번호, 치즈량 넣기
    for i in range(1,n+1):
        pizza_index = i
        oven.append((pizza_index, cheezes[pizza_index]))

    # 화덕 크기가 1초과일때까지
    while len(oven) > 1:
        # 오븐에서 피자 번호와 치즈를 꺼내 반으로 줄이기
        pizza_index, cheeze = oven.pop(0)
        cheeze //=2
        # 치즈가 0초과이면 다시 넣기
        if cheeze > 0:
            oven.append((pizza_index, cheeze))
        else:
            # 치즈가 0이하이면 대기중인 다음 피자 번호 넣기
            # 대기 중인 피자가 있는지 여부
            if waiting_pizza <= m:
                pizza_index = waiting_pizza
                waiting_pizza += 1
                oven.append((pizza_index, cheezes[pizza_index]))
    return oven[0][0]

T = int(input())
for t in range(1,T+1):
    n,m = list(map(int, input().split())) #화덕크기, 피자개수 
    cheezes = [0]+list(map(int, input().split()))
    print(pizza(n,m,cheezes))
