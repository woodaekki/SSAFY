def solve(a, b, c):
    eat = 0
    while a >= b:
        a -= 1
        eat += 1
    while b >= c:
        b -= 1
        eat += 1
      
    # b를 줄였을때 a보다 다시 같거나 줄었을 수 있으므로 한번더 체크 
    while a >= b:
        a -= 1
        eat += 1
  
    if 1 <= a and 1 <= b and 1 <= c and a < b < c:
        return eat
    else:
        return -1
  
T = int(input())
for t in range(1, T+1):
    a, b, c = list(map(int, input().split()))
    result = solve(a, b, c)
    print(f'#{t} {result}')