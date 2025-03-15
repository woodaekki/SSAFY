import sys
sys.stdin = open("tree.txt", "r")

def binary():
    value = m
    remained = "" 
    while value > 0:
        remain = value % 2
        remained = str(remain) + remained
        value = value // 2
    remained = remained.zfill(len_m*4)
    # print(remained) 
    scope = remained[-n:]
    # print(scope)
    if '0' in scope:
        return "OFF"
    else:
        return "ON"

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    len_m = len(str(m))
    result = binary()
    print(f'#{t} {result}')