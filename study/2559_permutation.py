# def permu():
#     n, k = list(map(int, input().split())) # 전체 날짜의 수, 연속적인 날짜의 수
#     days = list(map(int, input().split()))

#     maxv = -9999999999999
#     for i in range(n-k+1):
#         sumv = 0
#         for j in range(i, i+k):
#             sumv += days[j]
#             if sumv > maxv:
#                 maxv = sumv
#     return maxv

# print(permu())

def permu():
    n, k = list(map(int, input().split())) # 전체 날짜의 수, 연속적인 날짜의 수
    days = list(map(int, input().split()))

    first = 0
    for i in range(0, k):
        first += days[i]
    
    max_days = first
    for j in range(k, n):
        first -= days[j-k]
        first += days[j] 
        # print(first)
        if first > max_days:
            max_days = first

    return max_days

print(permu())