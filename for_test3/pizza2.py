import sys
sys.stdin = open("pizza.txt", "r")

def pizza():
    oven = []  
    waiting_pizza = n + 1  
    
    # 화덕에 n개의 피자 넣기
    for i in range(1, n + 1):
        oven.append((i, cheezes[i]))  # (피자 번호, 치즈 양)
    
    # 치즈가 다 녹을 때까지 반복
    while len(oven) > 1:
        pizza_index, cheese = oven.pop(0)  # 피자 꺼내기
        cheese //= 2  # 치즈 녹이기
        # 치즈가 남아있으면 다시 넣고 
        if cheese > 0:
            oven.append((pizza_index, cheese))  
        # 치즈가 0이하이면 대기중인 다음 피자 넣기
        else:
            if waiting_pizza <= m:
                oven.append((waiting_pizza, cheezes[waiting_pizza]))  # 새 피자 넣기
                waiting_pizza += 1  # 다음 대기 피자 번호 증가
    
    # 마지막 남은 피자 번호 반환
    return oven[0][0]

T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    n, m = map(int, input().split())  # 화덕 크기 n, 피자 개수 m
    cheezes = [0] + list(map(int, input().split()))  # 치즈 양 리스트
    result = pizza()
    print(f'#{t} {result}')

