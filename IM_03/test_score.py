import sys
sys.stdin = open("test.txt", "r")


def solve():
    pass

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))  
