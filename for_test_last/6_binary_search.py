import sys
sys.stdin = open("1.txt", "r")

def recur(left, right, target, recent_direction):
    global cnt
    # 종료 조건
    if left > right:
        return 0
    # 연속 왼,왼 / 오,오 일 경우에 종료
    mid = (left+right)//2
    # 타겟이 정위치일 경우
    if target == a[mid]:
        return 1

    # 타겟이 왼쪽에 있을 경우
    elif target < a[mid]:
        # 왼,왼 일 경우 종료
        if recent_direction == -1:
            return 0
        return recur(left, mid-1, target, -1)

    # 타겟이 오른쪽에 있을 경우
    else:
        # 오,오 일 경우 종료
        if recent_direction == 1:
            return 0
        return recur(mid+1, right, target, 1)

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 이진 탐색은 정렬한 상태로 시작할 것 !
    a.sort()
    cnt = 0
    for i in range(m):
        target = b[i]
        cnt += recur(0, n-1, target, 0)
    print(f'#{t} {cnt}')