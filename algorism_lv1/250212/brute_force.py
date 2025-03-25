# 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식

# 찾을 패턴이 원본군에 있는지 찾고, 있다면 그 길이를 반환해라.
def bruteforce(t, p):
    n = len(t)
    m = len(p)
    i = j = 0
    while i < n and j < m: # 패턴을 찾으면 중단
        # 패턴을 못찾은 경우
        if t[i] != p[j]:
            i = i-j+1 # j: 온만큼 빼주고, 1: 한칸 뒤로 가 다시 매칭 시작
            j = 0 # 다시 시작점으로

        # 패턴 찾은 경우 둘다 계속 한 칸씩 뒤로 가며 매칭 진행
        else:
            i += 1
            j += 1

    if j == m: # 끝까지 간 경우(실패해서 앞으로 돌아가지 않음 = 즉 끝까지 매칭됨)
        return i - m # i부터 온 j만큼 반환: 찾은 패턴의 길이
    else:
        return -1

t = 'zzzabcdabcdabcefabcd' # 원본군
p = 'abcdabcef' # 찾을 패턴
print(bruteforce(t, p))

# 찾으려는 패턴이 원본군에 몇 개 존재하는지 개수 반환해라.
def pattern_count(t, p):
    n = len(t)
    m = len(p)
    i = j = 0
    cnt = 0
    while i < n: # 원본 길이 끝까지 가는 동안
        # 패턴을 못찾은 경우
        if t[i] != p[j]:
            i = i-j+1 # j: 온만큼 빼주고, 1: 한칸 뒤로 가 다시 매칭 시작
            j = 0 # 다시 시작점으로

        # 패턴 찾은 경우 둘다 계속 한 칸씩 뒤로 가며 매칭 진행
        else:
            i += 1
            j += 1

        # 패턴을 찾은 경우
        if j == m:
            cnt += 1
            i = i -j+1
            j = 0

    return cnt

t = 'TTTTTATTAATA'
p = 'TTA'
print(pattern_count(t, p))

# 패턴이 매칭되었을 때, 찾은 위치값 반환해라.
def pattern_idx(t, p):
    n = len(t)
    m = len(p)
    i = j = 0

    while i < n: # 원본 길이 끝까지 가는 동안
        # 패턴을 찾은 경우
        if t[i] == p[j]:
            i += 1
            j += 1

            # 패턴을 찾은 경우 찾은 인덱스 반환
            if j == m:
                return i-m

        # 패턴 못찾은 경우 둘다 계속 한 칸씩 뒤로 가며 매칭 진행
        else:
            i = i - j + 1  # j: 온만큼 빼주고, 1: 한칸 뒤로 가 다시 매칭 시작
            j = 0  # 다시 시작점으로

    return -1

t = 'eoggxypvsy'
p = 'xypv'
print(pattern_idx(t, p))
