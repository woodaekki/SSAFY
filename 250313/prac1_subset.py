arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

# 1인 bit 수를 반환하는 함수
def cafe(target):
    cnt = 0
    for i in range(n):
        if target & 0x1:
            # print(arr[i], end = '')
            cnt += 1
        target >>= 1
    return cnt

# 모든 부분 집합 중 원소의 수가 2개 이상인 집합의 수
answer = 0
for target in range(0, 1<<n):
    if cafe(target) >= 2:
        answer += 1
print(answer)