import sys
sys.stdin = open("5204.txt", "r")

def merging(left, right):
    global cnt 
    # l = r = 0, left, right 리스트에서 비교하며 정렬 후 병합
    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1
    
    # 남은 리스트들이 있다면 담기 
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1
    
    # 오른쪽 원소가 먼저 복사되는 경우
    # 오른쪽 원소가 왼쪽보다 작을 때 
    # [5, 7]과 [1, 2, 4] 이라면, 이미 정렬된 상태이므로
    # 마지막 원소끼리만 비교하여 오른쪽이 더 작으면 먼저 복사될 것임 
    if left[-1] > right[-1]:
        cnt += 1
    return result

def merge_sort(ar):
    # 길이가 1이 되면, 그 원소를 반환
    if len(ar) == 1:
        return ar

    # 반을 계속 쪼갠다
    mid = len(ar) // 2
    left = ar[:mid]
    right = ar[mid:]

    # 분할이 완료되면
    a = merge_sort(left)
    b = merge_sort(right)

    # 병합함수 호출
    merged_list = merging(a, b)
    return merged_list

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    final_result = merge_sort(arr)
    # print(final_result)
    print(f'#{t} {final_result[n//2]} {cnt}')