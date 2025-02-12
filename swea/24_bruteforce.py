import sys
sys.stdin = open("brute.txt", "r",encoding='UTF-8')

def bruteforce():
    tc = int(input()) # 테스트 케이스 번호
    p = input() # 찾으려는 문자
    t = input() # 원본군

    m = len(p)
    n = len(t)

    cnt = 0 # 특정 문자열을 찾은 개수
    for i in range(n - m + 1):
        for j in range(m):
            if t[i + j] != p[j]:
                break
        else:
            cnt += 1
    return cnt

T = 10
for t in range(1, T+1):
    print(f'#{t} {bruteforce()}')
