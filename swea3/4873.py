import sys
sys.stdin = open("banbok.txt", "r")

def banbok(arr):
    stack = []
    stack.append(arr[0])
    for i in range(1, len(arr)):
        if stack and stack[-1] == arr[i]:
            stack.pop()
        else:
            stack.append(arr[i])
    
    leng = 0
    for j in stack:
        leng += 1
    return leng

T = int(input())
for t in range(1, T+1):
    arr = list(input())
    result = banbok(arr)
    print(f'#{t} {result}')