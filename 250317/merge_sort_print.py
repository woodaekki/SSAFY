def merge(left, right, depth=0):
    indent = "  " * depth
    print(f"{indent}Merging {left} and {right}")
    result = [0] * (len(left) + len(right))
    l = r = 0


    # 일단 받은 리스트 내에서~ 정렬
    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:                  # 왼쪽이 더 크다면
            result[l + r] = left[l]
            l += 1
        else:                                   # 오른쪽이 더 크다면
            result[l + r] = right[r]
            r += 1

    # 이제 분할되서 정렬된 애들을 다시 합쳐서 정렬!

    # 왼쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        print(f'result[l : {l}  + r : {r}] = left[l] : {left[l]}')
        l += 1

    # 오른쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while r < len(right):
        result[l + r] = right[r]
        print(f'result[l : {l} + r :{r}] = right[r] : {right[r]}')

        r += 1

    print(f"{indent}Result of merge: {result}")
    return result


def merge_sort(li, depth=0):
    indent = "  " * depth
    print(f"{indent}Sorting: {li}")
    # 기저 조건: 리스트의 길이가 1이면 이미 정렬된 상태
    if len(li) == 1:
        print(f"{indent}Base case reached: {li}")
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
    print(f"{indent}After merging: {merged}")
    return merged


# 예제 리스트
arr = [69, 10, 30, 2, 16, 8, 31, 22]
print("Starting Merge Sort")
sorted_arr = merge_sort(arr)
print("Final sorted list:", sorted_arr)