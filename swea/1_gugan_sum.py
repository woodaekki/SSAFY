def gugan_sum(n, m, arr):
    max_total = -9999999
    min_total = 9999999
    # 1. 구간 자르기
    for i in range(0, n - m + 1):
        idx = arr[i: i + m]
        # 2. 자른 구간의 합
        total = 0  
        for num in idx:  
            total += num  
        # 최대 합, 최소 합
        if total > max_total:
            max_total = total
        if total < min_total:
            min_total = total
    return max_total - min_total


t1 = gugan_sum(10, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # 리스트의 길이, 구간개수, 리스트 내부항목
t2 = gugan_sum(10, 5, [6262, 6004, 1801, 7660, 7919, 1280, 525, 9798, 5134, 1821])
print(t1, t2)