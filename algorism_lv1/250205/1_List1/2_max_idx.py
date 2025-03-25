# 배열 원소 중 최댓값의 인덱스 max_idx 찾기
# (최댓값이 여러개인 경우 마지막 인덱스로)
def max_func(arr, n): # 배열리스트, 원소 수
    max_idx = 0  # 첫번째 인덱스를 최댓값으로 가정
    for i in range(1, n):
        if arr[i] >= arr[max_idx]:
            max_idx = i
    return max_idx

idx = max_func([1, 4, 2, 5, 100, 100, 4], 6)
print(idx)