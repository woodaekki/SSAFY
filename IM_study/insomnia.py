import sys
sys.stdin = open("1.txt", "r")

def solve():
    visited = set()
    for i in range(1,10**6):
        nums = str(n * i)
        for num in nums:
            visited.add(num)
            if len(visited) == 10:
                return nums

T = int(input())
for t in range(1, T+1):
    n = int(input())
    result = solve()
    print(f'#{t} {result}')



