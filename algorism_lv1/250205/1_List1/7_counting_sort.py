# 집합에 각 항목이 몇 개씩 있는지 세는 알고리즘

# 0 <=  data[i] <= 4 조건 ( data 내부의 인덱스 개수가 4개 이하)
def counting_sort(n, data):
    if n == 0:
        return []
    
    max_value = max(data)  # 최대값 찾기 (음수가 없다고 가정)
    counts = [0] * (max_value + 1)  # 개수 카운트 리스트
    temp = [0] * n  # 정렬된 결과 저장 리스트
    
    # 1. 내부 항목들의 개수 세기
    for num in data:
        counts[num] += 1
    
    # 2. counts[i]까지의 합계
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    
    # 3. 정렬 결과를 temp에 저장 (뒤에서부터!)
    for i in range(n - 1, -1, -1):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]
    
    return temp

sorted_data = counting_sort(8, [0, 4, 1, 3, 1, 2, 4, 1])
print(sorted_data)  # [0, 1, 1, 1, 2, 3, 4, 4]

