import sys
sys.stdin = open("two.txt", "r")

def blog(n, x, arr):
    cnt = 1
    visitor = sum(arr[:x])
    max_visitor = visitor
    for i in range(1, n-x+1):
        visitor -= arr[i-1]
        visitor += arr[i+x-1]
        if visitor > max_visitor:
            max_visitor = visitor
            cnt = 1
        elif max_visitor == visitor:
            cnt += 1
    # 최대 방문자 수가 0명인 경우 "SAD" 출력
    if max_visitor == 0:
        return ["SAD"]
    return max_visitor, cnt

n, x = list(map(int, input().split())) # 일수, 기간
arr = list(map(int, input().split()))
result = blog(n, x, arr)
for re in result:
    print(re)