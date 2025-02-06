# 집합에 각 항목이 몇 개씩 있는지 세는 알고리즘

# 0 <=  data[i] <= 4 조건 ( data 내부의 인덱스 개수가 4개 이하)
data = [0, 4, 1, 3, 1, 2, 4, 1]
n = len(data)
counts = [0] * 5 # max(data) + 1, data 리스트 내부에 음수 존재할 경우 길이값 x
temp = [0] * n # 정렬 결과 저장
# 1. 내부 항목들의 개수 세기
for i in range(n):
    counts[data[i]] += 1

# print(counts) # [1, 3, 1, 1, 2]

# 2. counts[i]까지의 합계
for i in range(1, 5):
    counts[i] += counts[i - 1]

# print(counts) # [1, 4, 5, 6, 8]

# 3. 내부 항목들의 카운트를 위한 공간 할당 (뒤에서부터!!)
for i in range(n - 1, -1, -1):
    counts[data[i]] -= 1
    temp[counts[data[i]]] = data[i]
# print(temp)
