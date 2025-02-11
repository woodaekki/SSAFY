def palindrome():
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == s[i-1]:
            return 1
    return 0

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {palindrome()}')