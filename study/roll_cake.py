import sys
sys.stdin = open("2.txt", "r")

def rollcake():
    l = int(input())  # 롤케이크 길이
    n = int(input())  # 손님 수
    rollcake = [0] * (l + 1)  
    expected = [0] * (n + 1)
    
    for i in range(1, n + 1):  
        p, k = list(map(int, input().split()))  # p에서 k까지
        expected[i] = k - p + 1          
        for j in range(p, k + 1):
            if rollcake[j] == 0:
                rollcake[j] = i 

    # 기대 방청객 
    max_expected = max(expected[1:])  
    max_expected_idx = expected.index(max_expected) 

    num = [0] * (n + 1)  
    for cake in rollcake:
        if cake > 0:
            num[cake] += 1
    
    # 실제 방청객 
    max_actual = 0
    max_actual_idx = 0
    for i in range(1, n + 1):
        if num[i] > max_actual:
            max_actual = num[i]
            max_actual_idx = i

    return max_expected_idx, max_actual_idx

result = rollcake()
for re in result:
    print(re)
