def powerset(k):
    if k == n:
        sumv = 0

        # 부분집합의 합 구하기
        for i in range(n):
            if result[i] == 1: # 부분집합에 포함된 원소일 경우 
                sumv += arr[i]
        print(result, "->", sumv)

        # 원소의 합이 5인 경우만
        if sumv == 5:
            for i in range(n):
                if result[i] == 1: # 부분집합에 포함된 원소의 인덱스만 출력
                    print(arr[i], end = " ")
            print()
        # print(result)
        return

    candidates = [1, 0] # 1은 포함, 0은 포함x 을 의미 
    for i in candidates:
        result[k] = i  # k번째 원소를 포함(1) 또는 제외(0)
        powerset(k+1)

n = 4
arr = [1, 2, 3, 4]
result = [-1] * 4
powerset(0)
