# lev: 점원의 수
# bran: 점원 포함 o, x
def recur(cnt, total_height):
    global ans
    # 이미 b 이상인 탑이면, 점원을 더 쌓을 필요가 없음
    if total_height >= b:
        ans = min(ans, total_height)
        return
 
    if cnt == n:
        return
 
    recur(cnt+1, total_height + heights[cnt]) # 탑에 포함 o
    recur(cnt+1, total_height) # 탑에 포함 x
 
T = int(input())
for t in range(1, T + 1):
    n, b = list(map(int, input().split())) # 점원의 수, 탑의 높이
    heights = list(map(int, input().split()))
    ans = float("inf")
    recur(0, 0)
    print(f'#{t} {ans-b}')