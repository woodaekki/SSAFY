import sys
sys.stdin = open("1.txt", "r")

def millionaire():
    # 최댓값 구하기
    max_arr = arr[0]
    for i in range(n):
        max_arr = max(max_arr, arr[i])

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'{t} {millionaire()}')