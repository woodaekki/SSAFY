import sys
sys.stdin = open("2.txt", "r")

def solve():


T = int(input())
for t in range(1, T+1):
    n = int(input()) # 신청서 수
    start, end = list(map(int, input().split()))
    print(f'#{t} {solve()}')