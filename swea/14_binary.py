import sys
sys.stdin = open("binary.txt", "r")

T = int(input())

def binary():
    p, a, b = list(map(int, input().split())) # 전체 쪽수, 찾을 쪽수 a, b

    start = 1
    end = p
    middle = (start + end) // 2
    cnt_a = cnt_b = 0

    while start <= middle:
        middle = (start + end) // 2 # 중앙값은 매번 시작점과 끝점의 절반
        cnt_a += 1 # 돌아올때마다 카운트 1증가
        if a == middle:
            break
        elif a > middle: # 중앙값보다 크면
            start = middle # 시작점이 중앙값이 됨
        else: # 중앙값보다 작으면
            end = middle # 끝점이 중앙값이 됨

    start = 1
    end = p
    middle = (start + end) // 2
    while start <= middle:
        cnt_b += 1
        middle = (start + end) // 2
        if b == middle:
            break
        elif b > middle:
            start = middle
        else:
            end = middle

    # print(cnt_a)
    # print(cnt_b)
    if cnt_a < cnt_b:
        ans = "A"
    elif cnt_a > cnt_b:
        ans = "B"
    else:
        ans = 0
    return ans

for t in range(1, T+1):
    result = binary()
    print(f'#{t} {result}')



