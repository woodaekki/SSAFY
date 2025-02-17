# import sys
# sys.stdin = open("algo1_sample_in.txt", "r")

def flag():
    n, m = list(map(int, input().split()))  # 배열의 길이, 몇줄 받을 건지
    arr = list(map(int, input().split()))  # 0, 1, 1, 0, 0
    for _ in range(m):
        a, b, c = list(map(int, input().split()))  # 난이도, 기준번호, 기준번호부터 몇명바꿀건지
        for scope in range(b-1, b-1+c):
            if 0 <= scope < n:
                arr[scope] = 1 - arr[scope]
            # print(arr)
    return arr

T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end = " ")
    result = flag()
    print(*result)