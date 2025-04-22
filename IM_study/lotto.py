import sys
sys.stdin = open("1.txt", "r")

from itertools import combinations

def solve():
    new_arr = list(combinations(arr, 6))
    return new_arr

while True:
    ar = list(map(int, input().split()))
    if ar[0] == 0:
        break
    k, arr = ar[0], ar[1:]
    result = solve()
    for re in result:
        print(re[0], re[1], re[2], re[3], re[4], re[5])
    print()
