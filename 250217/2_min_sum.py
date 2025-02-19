import sys
sys.stdin = open("min_sum.txt", "r")

def f(i, n, s): # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global maxv
    # global cnt

    # cnt += 1
    if i == n:  # 마지막까지 다 돌고
        if maxv > s: # 합이 최소이면 갱신 
            maxv = s
    elif maxv < s:
        return
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]  # 자리교환 ([0,1,2][1,0,2][2,1,0])
            f(i+1, n, s+ar[i][p[i]])   # i+1번째 줄의 모든 조합인 p[i]를 다 더해서 최소합 경우 알아내고
            p[i], p[j] = p[j], p[i]  # 원상 복구하기 
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    ar = [list(map(int, input().split())) for _ in range(n)]
 
    p = []
    for i in range(n):
        p.append(i)

    maxv = 10000
    # cnt = 0 # 재귀호출 횟수 저장
    f(0, n, 0)
    print(f'#{t} {maxv}')