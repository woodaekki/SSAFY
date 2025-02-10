# 자료의 중앙에 있는 원소를 골라 (//2) <- 길이 값이 짝수 개여도 마찬가지
# 중앙원소와 찾고자 하는 목표 값 비교한다.
# 목표 값이 중앙 원소보다 작으면 왼쪽 반에 대해 검색 수행
# 크다면 오른쪽 반에 대해 검색 수행

def bianary_search(n, arr, key):
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2 # 중앙값
        if arr[middle] == key: # 목표값이 중앙값과 같으면 중앙값 반환
            return middle
        elif key < arr[middle]: # 목표값이 중앙값보다 작으면
            end = middle - 1 # e구간을 왼쪽으로 가게하여 앞구간 검색
        else: # 목표값이 중앙값보다 크면
            start = middle + 1 # s구간을 오른쪽으로 가게하여 뒷구간 검색
    return -1

result = bianary_search(7, [2, 4, 7, 9, 11, 19, 23], 19)
print(result)