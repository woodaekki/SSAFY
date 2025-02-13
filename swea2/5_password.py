import sys
sys.stdin = open("pascal.txt", "r")

def password():
    n, ar = list(map(str, input().split())) # 길이값, 문자열
    i = 0
    arr = list(ar)
    while i < len(arr) -1:
        if arr[i] != arr[i+1]:
            i += 1
        else:
            arr.pop(i)
            arr.pop(i)
            i = 0
    return "".join(arr)


T = 10
for t in range(1, T+1):
    print(f'#{t} {password()}')