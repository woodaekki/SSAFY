# 순회하며, 키 값이 동일한 원소를 찾으면, 그 원소의 '인덱스' 반환
# 찾지 못하면 검색 실패

def sequential_search(arr, n, key):
    for i in range(0, n):
        if arr[i] == key: #찾고자 하는 원소
            return i
    return -1

result = sequential_search([1, 5, 3, 6, 4], 5, 4)
print(result)

# if 2차원의 경우라면
def sequential_search2(arr, n, key):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == key:
                return 1 # 키가 있으면 1
    return 0

result2 = sequential_search2([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 5)
print(result2)

# if, 오름차순 정렬된 상태에서 검색한다면
# 순회하며, 원소의 키 값이 검색 대상의 키 값보다 크면
# 찾는 원소가 없으므로 검색 종료

def sequential_search3(arr, n, key):
    for i in range(0, n):
        if arr[i] == key:
            return i
        elif arr[i] > key:
            return -1
    return -1 # 모든 원소가 key보다 작으면

result3 = sequential_search3([1, 3, 4, 5, 8], 5, 4)
print(result3)