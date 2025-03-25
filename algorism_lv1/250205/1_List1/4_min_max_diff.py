# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하라.
def min_max_diff(n, arr):
    maxv = 0
    minv = 999999999
    for i in range(n):
        if arr[i] > maxv:
            maxv = arr[i]
        if arr[i] < minv:
            minv = arr[i]
    return maxv - minv

t1 = min_max_diff(5, [477162, 658880, 751280, 927930, 297191]) # 리스트 길이, 내부 항목 리스트트
t2 = min_max_diff(5, [565469, 851600, 460874, 148692, 111090])
t3 = min_max_diff(10, [784386, 279993, 982220, 996285, 614710, 992232, 195265, 359810, 919192, 158175])
print(t1, t2, t3) # 630739 740510 838110









