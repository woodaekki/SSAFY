import sys
sys.stdin = open("5207.txt", "r")

# b의 숫자들이 a에 저장되어있는지 보는 문제
# 왼쪽, 왼쪽 / 오른쪽, 오른쪽이면 탐색 중단
def binary_search_recur(left, right, target, recent_direction):
    global cnt
    # 못찾으면 0 반환
    if left > right:
        return 0

    mid = (left + right) // 2
    # 타겟을 찾으면 찾은 개수 1 증가 위해 1 반환
    if target == a[mid]:
        return 1

    # 타겟이 중앙을 기준으로 왼쪽에 있을 때
    if target < a[mid]:
        # 왼쪽, 왼쪽이면(-1) 탐색 중단
        if recent_direction == -1:
            return 0
        return binary_search_recur(left, mid-1, target, -1)
    # 오른쪽에 있을 때
    else:
        # 오른쪽, 오른쪽이면(+1) 탐색 중단
        if recent_direction == 1:
            return 0
        return binary_search_recur(mid+1, right, target, 1)

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split())) # 리스트 a, b의 길이
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    cnt = 0
    for i in range(m):
        target = b[i]
        cnt += binary_search_recur(0, n-1, target, 0)
    print(f'#{t} {cnt}')