def recur(left, right, target, recent_direction):
    mid = (left+right) // 2
    if a[mid] == target:
        return 1
    elif a[mid] > target:
        if recent_direction == -1:
            return 0
        return recur(left, mid-1, target, -1)
    else:
        if recent_direction == 1:
            return 0
        return recur(mid+1, right, target, 1)
 
T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split())) # b에 저장된 정수가 a에 몇개가 들어있는가
    # 이진 탐색은 정렬이 필수
    a.sort()
    cnt = 0
    for i in range(m):
        target = b[i]
        cnt += recur(0, n-1, target, 0)
    print(f'#{t} {cnt}')