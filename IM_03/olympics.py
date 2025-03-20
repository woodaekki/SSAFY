import sys
sys.stdin = open("olym.txt", "r")

def solve(n, m, a, b):
    vote = [0] * n
    for j in range(m):
        for i in range(n):
            if a[i] <= b[j]:
                vote[i] += 1
                break
    # print(vote)
    max_num = max(vote)
    sport = vote.index(max_num)
    return sport + 1

T = int(input())
for t in range(1, T + 1):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = solve(n, m, a, b)
    print(f'#{t} {result}')
