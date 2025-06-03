def stove():
    # 대기중인 남은 피자 인덱스
    waiting_pizza = n
 
    # 화덕에 피자가 하나만 남을 때까지
    while len(oven) > 1:
        # 오븐에서 피자의 인덱스와 치즈 pop
        index, cheese = oven.pop(0)
        # 치즈량 반으로 줄이기
        cheese = cheese // 2
 
        if cheese > 0: # 치즈가 0보다 크면 오븐에 다시 넣기
            oven.append((index, cheese))
        else:
            # 치즈가 0이면, 대기 중인 다음 피자 오븐에 넣기
            if waiting_pizza < m:  # 피자를 다 넣었다면
                # 새로운 피자 넣기 (대기중인 피자 인덱스, 치즈량 넣기)
                oven.append((waiting_pizza, cheezes[waiting_pizza]))
                waiting_pizza += 1  # 대기 중인 다음 피자 번호 갱신 
    return oven[0][0] + 1 # 피자 번호는 1번부터이니까 +1
 
T = int(input())
for t in range(1, T + 1):
    n, m = list(map(int, input().split()))  # 화덕 크기,피자 개수
    cheezes = list(map(int, input().split()))  # 치즈량
 
    oven = []
    # 피자 한바퀴 도는 동안 각 피자의 인덱스와 치즈량 저장
    for i in range(n):
        oven.append((i, cheezes[i]))
    print(f'#{t} {stove()}')