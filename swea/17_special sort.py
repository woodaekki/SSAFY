import sys
sys.stdin = open("special.txt", "r")
T = int(input())

def special_sort():
    n = int(input()) # 길이값
    arr = list(map(int, input().split()))

    # 1. 오름차순 정렬을 한다.
    for i in range(0, n-1):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    half = len(arr) // 2
    for k in range(0, len(arr)):
        # 2. 짝수 인덱스일때, 오름차순
        if k % 2 == 0:
            even = arr[0: half]
        # 3. 홀수 인덱스일때, 내림차순
        else:
            odd = arr[k: half-1: -1]

    # 4. 번갈아 내보내기
    result = []
    for ar in range(0, half):
        result.append(odd[ar])
        result.append(even[ar])
    return result[:10]


for t in range(1, T+1):
    special = special_sort()
    print(f'#{t}', end = " ")
    for sp in special:
        print(f'{sp}', end = " ")
    print()