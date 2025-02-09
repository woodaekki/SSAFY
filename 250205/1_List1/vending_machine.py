# 손님에게 거스름돈으로 주는 지폐와 동전의 개수를 최소한으로 줄이기

moneys = {50000: 0, 10000: 0, 5000: 0, 1000: 0} # 지폐의 종류
change = 1045000  # 내는 돈

# 각 지폐의 개수를 계산
for money in moneys.keys():
    # print(denomination)
    moneys[money] = change // money  # 몫 계산
    change = change % money  # 나머지 금액 갱신

# 결과 출력
for money, count in moneys.items():
    print(f"{money}원 지폐: {count}개")

