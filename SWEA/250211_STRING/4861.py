def palindrome():
    n, m = map(int, input().split())  # n x n, 문자열 길이
    arr = [list(input())  for _ in range(n)]  
     
    p = []
 
    # 가로로 회문일 때
    for i in range(n):
        for j in range(0, n-m+1):
            scope = arr[i][j:j+m] # 문자열 형태로 담김 
            if scope == scope[::-1]:
                p.append("".join(scope))
     
    # 세로로 회문일 때
    for j in range(n):
        for i in range(n-m+1):
            scope2 = []
            for k in range(m):
                scope2.append(arr[i+k][j])
            if scope2 == scope2[::-1]:
                p.append("".join(scope2))
 
    return "".join(p)
 
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {palindrome()}')