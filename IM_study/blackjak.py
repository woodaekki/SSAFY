import sys
sys.stdin = open("1.txt", "r")

from itertools import combinations

def solve():
    cards_lst = []
    min_diff = float('inf')
    cards = list(combinations(arr, 3))
    for i in range(len(cards)):
        if sum(cards[i]) <= m:
            cards_lst.append(sum(cards[i]))
    cards_lst.sort()
    return max(cards_lst)

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
result = solve()
print(result)