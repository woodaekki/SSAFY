# '도착지점 = 2' 을 찾아서 거슬러 올라간다.
# 1을 따라 위로 올라가는데
# 좌나 우방향에 1이 있으면 방향 전환을 한다.

# lft = (1, 0)
# rht = (0, 1) # 좌, 우

import sys
sys.stdin = open("ladder.txt", "r")

T = 10

def ladder():
    n = int(input()) # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 1. 도착지점 2의 col 값 찾기
    for col in range(0, 100):
        if 2 == arr[99][col]:
            start = col # 2의 위치 col 인덱스 저장

    # 2.1을 따라 위로 올라가다가 방향 전환하기
    for row in range(99, -1, -1): # 마지막 열부터 위로 올라감
        # 왼쪽 방향에 1이 있을 경우
        if 0 < start and arr[row][start-1] == 1:
            while 0 < start and arr[row][start-1] == 1:
                start -= 1

        # 오른쪽 방향에 1이 있을 경우
        elif start < 99 and arr[row][start+1] == 1:
            while start < 99 and arr[row][start+ 1] == 1:
                start += 1
    return start

for t in range(1, T + 1):
    print(f'#{t} {ladder()}')