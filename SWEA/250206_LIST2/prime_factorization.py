T = int(input())  
 
for t in range(1, T + 1):
    n = int(input())  # 정수
 
    a, b, c, d, e = 0, 0, 0, 0, 0  
 
    while n % 2 == 0:  # 2로 나누어 떨어지는 동안 계속 나눠라
        a += 1  # 카운트 횟수 1씩 증가
        n //= 2
    while n % 3 == 0:
        b += 1
        n //= 3
    while n % 5 == 0:
        c += 1
        n //= 5
    while n % 7 == 0:
        d += 1
        n //= 7
    while n % 11 == 0:
        e += 1
        n //= 11
 
    print(f"#{t} {a} {b} {c} {d} {e}")