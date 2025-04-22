import sys
sys.stdin = open("1.txt", "r")

from itertools import combinations

def solve():
    visited = set()
    for i in range(1,n+1):
        possible_scores = list(combinations(arr, i))
        # print(possible_scores)
        for j in range(len(possible_scores)):
            visited.add(sum(possible_scores[j]))
    return len(visited) + 1

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve()
    print(f'#{t} {result}')

