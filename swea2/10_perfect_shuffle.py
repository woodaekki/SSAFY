import sys
sys.stdin = open("shuffle.txt", "r")

def shuffle():
    n = len(arr)
    for i in range(n//2):
        if n % 2 == 1:
            front = arr[0: i+2]
            back = arr[i+2:n]

        elif n % 2 == 0:
            front = arr[0:i+1]
            back = arr[i+1:n]

    lst = []
    for i in range(n//2):
        lst.append(front[i])
        lst.append(back[i])

    # 홀수이면, 먼저 놓는 쪽에 한 장이 더 들어가도록
    if len(front) > len(back):
        lst.append(front[-1])

    return lst

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(str, input().split()))
    result = shuffle()
    print(f'#{t}', end=" ")
    print(*result)