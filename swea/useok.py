import sys
sys.stdin = open("eusok.txt", "r")

def seok():
    arr = [list(input()) for _ in range(5)]
    # 1. 리스트 중 가장 긴 줄의 길이
    mv = 0
    for ar in arr:
        if len(ar) > mv:
            mv = len(ar)

    # 2.
    num_row = 5
    for col in range(mv):
        for row in range(num_row):
            if col < len(arr[row]):
                print(arr[row][col], end = "")


T = int(input())
for t in range(1, T+1):
    print(f'#{t}')
