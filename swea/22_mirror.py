import sys
sys.stdin = open("mirror.txt", "r")

def mirror():
    arr = list(input())
    n = len(arr)

    # 1. 문자열 뒤집기
    for i in range(n // 2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

    # 2. 규칙에 따라 바꾸기
    for j in range(n):
        if arr[j] == 'q':
            arr[j] = 'p'
        elif arr[j] == 'p':
            arr[j] = 'q'
        elif arr[j] == 'd':
            arr[j] = 'b'
        elif arr[j] == 'b':
            arr[j] = 'd'
    return "".join(arr)


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {mirror()}')