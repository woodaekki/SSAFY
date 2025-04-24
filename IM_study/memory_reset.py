import sys
sys.stdin = open("1.txt", "r")

T = int(input())
for t in range(1, T+1):
    arr = list(input())
    cnt = 0
    change = '0'
    for ar in arr:
        if ar != change:
            change = ar
            cnt += 1
    print(f'#{t} {cnt}')


