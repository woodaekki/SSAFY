import sys
sys.stdin = open("1.txt", "r")

T = int(input())
for t in range(1, T+1):
    v, e = list(map(int, input().split()))
