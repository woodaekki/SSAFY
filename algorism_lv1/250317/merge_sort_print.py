def merge(left, right, depth=0):
    indent = "  " * depth
    print(f"{indent}{left} 와 {right} 를 병합 중")
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:  # 왼쪽 값이 더 작다면
            result[l + r] = left[l]
            l += 1
        else:  # 오른쪽 값이 더 작다면
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터를 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        print(f'result[l : {l}  + r : {r}] = left[l] : {left[l]}')
        l += 1

    # 오른쪽 리스트에 남은 데이터를 모두 result 에 추가
    while r < len(right):
        result[l + r] = right[r]
        print(f'result[l : {l} + r :{r}] = right[r] : {right[r]}')
        r += 1

    print(f"{indent}병합 결과: {result}")
    return result


def merge_sort(li, depth=0):
    indent = "  " * depth
    # print(f"{indent}정렬 중: {li}")
    # 기저 조건: 리스트 길이가 1이면 이미 정렬된 상태
    if len(li) == 1:
        # print(f"{indent}기본 조건 도달: {li}")
        return li

    # 리스트를 절반으로 분할
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    # 재귀 호출을 통해 각각 정렬
    sorted_left = merge_sort(left, depth + 1)
    sorted_right = merge_sort(right, depth + 1)

    # 분할이 완료되면 병합
    merged = merge(sorted_left, sorted_right, depth)
    # print(f"{indent}병합 후: {merged}")
    return merged


# 예제 리스트
arr = [69, 10, 30, 2, 16, 8, 31, 22]
# print("병합 정렬 시작")
sorted_arr = merge_sort(arr)
print("최종 정렬된 리스트:", sorted_arr)