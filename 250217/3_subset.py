def powerset(k):
    if k == n:
        sumv = 0
        for i in range(n):
            if result[i]:
                sumv += arr[i]
        print(result, "->", sumv)

        # 원소의 합이 10인 경우만
        if sumv == 10:
            for i in range(n):
                if result[i]:
                    print(arr[i], end = " ")
            print()
        # print(result)
        return

    candidates = [1, 0]
    for i in candidates:
        result[k] = i
        powerset(k+1)

n = 5
arr = [1, 2, 3, 4, 5]
result = [-1] * 5
powerset(0)
