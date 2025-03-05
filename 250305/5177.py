import sys
sys.stdin = open("5177.txt", "r")

T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
