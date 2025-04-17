import sys
sys.stdin = open("1.txt", "r")

def solve():
    total = 0
    for i in range(2, n-2):
        left1 = arr[i-2]
        left2 = arr[i-1]
        right1 = arr[i+1]
        right2 = arr[i+2]
        second_highest = max(left1, left2, right1, right2)
        if left1 < arr[i] and left2 < arr[i] and right1 < arr[i] and right2 < arr[i]:
            total += (arr[i]-second_highest)
    return total


T = 10
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve()
    print(f'#{t} {result}')
