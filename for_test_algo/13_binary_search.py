import sys
sys.stdin = open("2.txt", "r")

def recur(left, right, target, recent_direction):
    # 종료조건
    if left > right:
        return 0
    mid = (left+right) // 2
    if a[mid] == target:
        return 1
    elif a[mid] < target:
        if recent_direction == 1:
            return 0
        return recur(mid+1, right, target, 1)
    elif a[mid] > target:
        if recent_direction == -1:
            return 0
        return recur(left, mid-1, target, -1)

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split())) # a, b의 수
    a = list(map(int, input().split()))
    b = list(map(int, input().split())) # b에 저장된 수가 a에 있는지 여부
    # 이진탐색에서 가장 중요한 정렬 설정 잊지 말기 !!!
    a.sort()

    result = 0
    for j in range(m):
        target = b[j]
        result += recur(0, n-1, target, 0)
    print(f'#{t} {result}')