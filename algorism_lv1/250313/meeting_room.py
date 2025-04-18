import sys
sys.stdin = open("load.txt", "r")

"""
l = [(2, 6), (5, 1), (6, 2), (1, 10)]
def fun(x):
    return x[1]
    
a = sorted(l, key=lambda x:x[1])
"""

def load(s, e):
    global cnt
    # end 중심 오름차순 정렬하기
    lst.sort(key=lambda x: (x[1], x[0]))

    # end 기준 i번째 종료시간이 적은 것 선택
    s, e = lst[0]
    cnt += 1
    # print(s,e)
    for i in range(1, n):
        # print(lst[i][0])
        # 종료시간보다 시작시간이 크거나 같으면 넣기
        if lst[i][0] >= e:
            s, e = lst[i]
            cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    n = int(input())
    lst = []
    cnt = 0
    for _ in range(n):
        start, end = list(map(int, input().split()))
        lst.append((start, end))
    print(f'#{t} {load(start, end)}')