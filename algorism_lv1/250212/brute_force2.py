# for 문을 이용한 bruteforce

def bruteforce2(t, p):
    n = len(t)
    m = len(p)

    for i in range(n-m+1): # t에서 패턴을 비교할 시작 위치 인덱스
        for j in range(m): # p에서 비교할 위치 인덱스
            if t[i+j] != p[j]:
                break

        else: # break에 걸리지 않고 for 가 끝난 경우 실행
            return i # 패턴이 처음 나타난 인덱스 위치

    return -1 # 못찾은 경우

t = 'TTTTTATTAATA'
p = 'TTA' # 찾으려는 패턴
print(bruteforce2(t, p))