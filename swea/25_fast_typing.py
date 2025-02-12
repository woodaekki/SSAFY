import sys
sys.stdin = open("fast_typing.txt", "r",encoding='UTF-8')

def fast():
    t, p = map(str, input().split()) # 원본군, 단축키

    tp = pp = 0 # t와 p의 인덱스
    cnt = 0

    while tp < len(t):
        if t[tp] == p[pp]:
            tp += 1
            pp += 1
            if pp == len(p):
                cnt += 1
                pp = 0
        else:
            tp = tp - pp + 1 # 못찾으면 돌아가서
            pp = 0

    result = (len(t) - cnt * len(p)) + cnt
    return result


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {fast()}')

