def solve():
    cnt = 0
    scope = a[:len(a)]
    i = 0
    while i < len(b):
        if scope == b[i:i+len(a)]:
            i += len(a)
            cnt += 1
        else:
            i += 1
    return cnt

for _ in range(10):
    tc = int(input())
    a = input()
    b = input()
    result = solve()
    print(f'#{tc} {result}')