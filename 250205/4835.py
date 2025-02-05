T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(0, N - M + 1):
        # 1. 구간
        idx = arr[i: i+M]
        sum_num = 0
        # max_num = -999999999999
        # min_num = 9999999999999
        # print(idx)
        sum_list = []
        # 2. 각 구간의 합
        for num in idx:
            sum_num += num
        print(sum_num)

        # # 3. 최소 합, 최대 합
        # if num < min_num:
        #     min_num = num

    # print(f'#{t} {max_sum - min_sum}')

# 1. 0:3
# 2. 1:4
# 3. 2:5
#...7:10

