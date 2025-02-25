import sys
sys.stdin = open("rotation.txt", "r")

def rotation():
    cnt = 0
    while cnt < m:
        cnt += 1
        t = arr.pop(0)
        arr.append(t)
        # print(arr)
        # print(cnt)
    return arr[0]

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = rotation()
    print(f'#{t} {result}')