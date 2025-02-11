"""
4
cbbcbaab
cccbabcb
caaaacab
baccccac
aabcbbac
acaacabc
bccbaabc
abbbccaa
"""
# 1. 슬라이스로 회문인지 확인
# # 문자열 s를 입력받아 회문이면 True, 아니면 False 반환
def palindrome(s):
    if s == s[::-1]:
        return True
    return False
#
n = int(input())  # 문자열의 길이
arr = [input() for _ in range(8)]

cnt = 0
for row in range(8):
    for st in range(8-n+1):
        if palindrome(arr[row][st:st+n]):
            print(arr[row][st:st+n])
            cnt += 1
print(cnt)

# 2. 인덱스로 회문인지 확인
# 문자열 s를 입력받아 회문이면 True, 아니면 False 반환
def palindrome(s):
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            return False
    return True

n = int(input())  # 문자열의 길이
arr = [input() for _ in range(8)]

cnt = 0
for row in range(8):
    for st in range(8-n+1):
        if palindrome(arr[row][st:st+n]):
            print(arr[row][st:st+n])
            cnt += 1
print(cnt)

# 세로를 가로로 바꾸기
a = [1, 2, 3]
b = [11, 12, 13]
c = [21, 22, 23]
print(list(zip(a, b, c)))

# 3. 가로, 세로 배열의 회문 찾기
# 세로를 가로로 바꾸기
arr2 = list(zip(*arr))
# print(arr2)

cnt = 0
for row in range(8):
    for st in range(8-n+1):
        if palindrome(arr[row][st:st+n]):
            print(arr[row][st:st+n])
            cnt += 1
        # if palindrome(arr2[row][st:st+n]):
        #     print(arr2[row][st:st+n])
        #     cnt += 1
print(cnt)

# 세로 배열 가로로 안 바꾸고 회문 찾기
for col in range(8):
    for st in range(8-n+1):
        s = ''
        for row in range(st, st+n):
            s += arr[row][col]
        if palindrome(s):
            cnt += 1
            print(s)
print(cnt)