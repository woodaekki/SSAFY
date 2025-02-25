import sys
sys.stdin = open("password.txt", "r")

def password(arr):
    stack = []
    stack.append(arr[0])
    for i in range(1,len(arr)):
        if stack and stack[-1] == arr[i]:
            stack.pop()
        else:
            stack.append(arr[i])
    return "".join(stack)

T = 10
for t in range(1, T+1):
    n, arr = list(map(str, input().split()))
    print(f'#{t} {password(arr)}')