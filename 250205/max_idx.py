# 배열 원소 중 최댓값의 인덱스 max_idx 찾기

def max_func(arr, N): # 배열리스트, 원소 수
    max_idx = 0  # 첫번째 인덱스를 최댓값으로 가정
    for i in range(1, N):
        if arr[max_idx] < arr[i]:
            max_idx = i
    return max_idx

idx = max_func([1, 4, 2, 5, 100, 4], 6)
print(idx)