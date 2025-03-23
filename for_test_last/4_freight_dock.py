import sys
sys.stdin = open("1.txt", "r")

def solve(start, end):
    # 종료시간 기준 오름차순 정렬
    arr.sort(key = lambda x:x[1])
    start, end = arr[0]
    cnt = 1 # 한 개 적재함
    # 종료시간 보다 시작시간이 크거나 같으면 넣기
    for i in range(1, n):
        if arr[i][0] >= end:
            cnt += 1
            start, end = arr[i]
    return cnt

T = int(input())
for t in range(1, T+1):
    n = int(input()) # 신청서 수
    arr = []
    for _ in range(n):
        start, end = list(map(int, input().split()))
        arr.append((start, end))
    result = solve(start, end)
    print(f'#{t} {result}')