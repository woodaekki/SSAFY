T = int(input())
 
for t in range(1, T+1):
    n, k= list(map(int, input().split())) # 부분집합의 원소의 수, 부분집합의 합
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
 
    #   1. arr의 길이 구하기
    m = 0
    for _ in arr:
        m += 1
 
    count = 0 # 조건을 만족하는 부분집합의 개수
 
    # 2. 부분집합을 순회하면서 합이 k인 부분집합을 찾기
    for i in range(2**m):  # 2**n개 만큼 모든 부분집합 순회
        subset_sum = 0
        subset = []
        for j in range(m):  # 원소의 수만큼 비트 비교
            if i & (1 << j):  # 모든 부분 집합의 경우의 수 찾기
                subset.append(arr[j])
        # print(subset)
                subset_sum += arr[j]
         
        # 3. 조건을 만족하는 부분집합의 총 개수
        if len(subset) == n and subset_sum == k:  
            count += 1
     
    print(f'#{t} {count}')