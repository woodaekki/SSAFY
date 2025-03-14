import sys
sys.stdin = open("input.txt", "r")

def binary():
    remained = ""
    value = m
    while value > 0:
        remain = value % 2
        remained = str(remain) + remained
        value = value // 2
    remained = remained.zfill(4 * str_m) # 0 채우기
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
    str_m = len(str(m))
    print(f'#{t} {binary()}')