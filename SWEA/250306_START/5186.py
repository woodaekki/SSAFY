def binary(n):
    cnt = 0
    ans = ""
    while 0 < n < 1 and cnt < 13:
        n = n * 2
        if n >= 1:
            ans += "1"
            cnt += 1
            n -= 1
        else:
            ans += "0"
            cnt += 1
     
    if cnt >= 13:
        return "overflow"
    return ans
     
T = int(input())
for t in range(1, T+1):
    n = float(input())
    result = binary(n)
    print(f'#{t} {result}')