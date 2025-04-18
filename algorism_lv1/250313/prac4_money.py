# 동전 교환
coin_lst = [500, 100, 50, 10]
target = 1730
cnt = 0

for coin in coin_lst:
    possible_cnt = target // coin
    cnt += possible_cnt
    target -= coin * possible_cnt
print(cnt)