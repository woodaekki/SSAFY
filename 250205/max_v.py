# 배열 원소 중 최댓값 max_v 찾기
def max_func(arr, N): # 배열리스트, 원소 수
    max_v = 0
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
    return max_v

max_num = max_func([1, 3, 4, 2, 10], 5)
print(max_num)
