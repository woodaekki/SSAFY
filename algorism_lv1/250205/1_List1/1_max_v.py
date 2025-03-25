# 배열 원소 중 최댓값 max_v 찾기
def max_func(arr, n): # 배열리스트, 원소 수
    maxv = 0
    for i in range(n):
        if arr[i] > maxv:
            maxv = arr[i]
    return maxv

max_num = max_func([1, 3, 4, 2, 10], 5)
print(max_num)
