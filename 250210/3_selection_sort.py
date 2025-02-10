# 최솟값을 찾는다
# 리스트의 맨 앞의 위치값과 교환 (맨앞의 원소 위치를 최소라고 가정)
# 다시 최솟값을 찾는다
# 리스트의 맨 앞의 위치값과 교환
# 반복한다.

def selection_sort(arr, n):
    for i in range(0, n-1):
        min_idx = i # 맨앞의 원소를 최소로 가정
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # 최소 원소 위치 갱신
    return arr

result = selection_sort([11, 10, 25, 64, 22], 5)
print(result)