import sys
sys.stdin = open("test.txt", "r")  # 디버깅 시 주석 처리 가능

def solve(n, arr):  # n과 arr을 매개변수로 추가


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve(n, arr)  # n과 arr을 전달
    print(result)
