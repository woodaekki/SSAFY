import sys
sys.stdin = open("banbok.txt", "r")

def banbok():
    arr = list(input())
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i += 1
    return len(arr)

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {banbok()}')