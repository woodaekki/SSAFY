T = int(input())  
for t in range(1, T + 1):
    N, M = map(int, input().split())  # 리스트 내 항목 수 N, 구간 수 M
    arr = list(map(int, input().split())) 

    # 초기화 값 위치 조심 !!!
    max_total = -9999999
    min_total = 9999999
    # 1. 구간  
    for i in range(0, N - M + 1):
        idx = arr[i: i + M]

        # 2. 구간의 합
        total = 0  
        for num in idx:  
            total += num  

        # 3. 최대 합, 최소 합
        if total > max_total:
            max_total = total
        if total < min_total:
            min_total = total
    
    print(f'#{t} {max_total -  min_total}')