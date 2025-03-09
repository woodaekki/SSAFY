import sys
sys.stdin = open("1.txt", "r")

def binary():
    remained = ""
    value = m
    len_m = len(str_m)
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
    str_m = str(m)
    result = binary()
    print(f'#{t} {result}')
    