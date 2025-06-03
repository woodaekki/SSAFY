T = 10
for t in range(1, T+1): # 총 테스트 케이스 개를 입력받음
    tc = int(input()) # 테스트 케이스 번호 입력
    arr = [list(map(int, input().split())) for _ in range(100)] # 가로줄 100개 입력받음
    row_sum = [0] * 100
    col_sum = [0] * 100
 
    sum = 0
 
    # # 가로합
    for i in range(100):
        for j in range(100):
            row_sum[i] += arr[i][j]
 
    # # 100줄 중에서 최댓값 구하기
    maxv = 0
    for num in row_sum:
        if num > maxv:
            maxv = num
    # # print(maxv)
 
    # 세로합
    for i in range(100):
        for j in range(100):
            col_sum[j] += arr[i][j]
 
    # # 100줄 중에서 최댓값 구하기
 
    maxv2 = 0
    for num in col_sum:
        if num > maxv2:
            maxv2 = num
    # print(maxv2)
 
    # 대각선합
    sum1, sum2 = 0, 0
    for i in range(100):
        sum1 += arr[i][i] # 좌에서 우로 내려가는 대각선
        sum2 += arr[i][100 - 1 - i] # 우에서 좌로 내려가는 대각선
 
    print(f'#{t} {max(maxv, maxv2, sum1, sum2)}')