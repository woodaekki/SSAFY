# 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1에 idx에 넣기
N, V = map(int, input().split()) # N, 찾는 값 V
arr = list(map(int, input().split()))

def find_idx():
    idx = -1
    for i in range(N):
        if arr[i] == V: # arr[i]가 찾는 값이면 
            idx = i
            break
    return idx

print(idx)