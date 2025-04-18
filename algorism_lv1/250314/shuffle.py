import sys
sys.stdin = open("shuffle.txt", "r")

def shuffle():
    print(f'#{t}', end=" ")
    left = 0
    right = (n+1)//2
    for i in range((n+1)//2):
        #왼쪽출력
        print(arr[left], end=' ')
        left += 1
        if right < n:
            print(arr[right], end=' ')
            right += 1

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(str, input().split()))
    shuffle()
    print()