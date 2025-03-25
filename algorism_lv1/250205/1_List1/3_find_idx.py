# 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1에 idx에 넣기
def find_idx(n, v, arr):
    v_idx = -1 # 찾는 값의 인덱스 저장
    for i in range(n):
        if arr[i] == v:
            v_idx = i
            break; # 찾는 순간 멈추기
    return v_idx 

idx = find_idx(6, 5, [2, 7, 5, 3, 1, 7]) # 리스트 길이, 찾는 값, 리스트
print(idx)

