import sys
sys.stdin = open("1.txt", "r")


def solve():
    cnt = 1
    end = arr[0][1]

    for i in range(1, len(arr)):
        if arr[i][0] >= end:
            cnt += 1
            end = arr[i][1]
    return cnt

T = int(input())
arr = []
for _ in range(T):
    s, e = list(map(int, input().split()))
    arr.append((s, e))
arr.sort(key=lambda x: (x[1], x[0]))
result = solve()
print(result)




