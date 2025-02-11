import sys
sys.stdin = open("palin.txt", "r")

def palindrome():
    n, m = map(int, input().split())  # n x n, 문자열 길이
    arr = [input()  for _ in range(n)]  # 문자열 리스트 입력 받기
    p = []

    # 가로로 회문일 때
    for ar in arr:
        if ar == ar[::-1]:
            p.append(ar)

    # 세로로 회문일때
    arr1 = list(zip(*arr))
    for ar1 in arr1:
        if ar1 == ar1[::-1]:
            p.append(ar1)
    return p

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {palindrome()}')