import sys
sys.stdin = open("st.txt", "r")

def recur(row, start):
    global min_diff
    if row >= n:
        return

    # 1. 팀원 구성하기 !
    # 스타트 팀에 추가하는 경우
    recur(row + 1, start + [row])
    # 스타트 팀에 추가하지 않는 경우
    recur(row + 1, start)

    # 스타트 팀에 없는 팀원은 다 링크 팀 팀원
    link = []
    for i in range(n):
        if i not in start:
            link.append(i)

    # 지선생님이 추가해주신 부분
    # 근데 갠적으로 인원이 짝수고,
    # 스타트팀 아니면 다 링크팀에 들어가게 했는데
    # 이 부분 차이로 정답이 갈리는 이유를 모르겠음.
    # 링크 팀과 스타트 팀의 인원이 같은지 확인
    if len(link) != len(start):
        return

    # 2. 점수 계산하기 !
    # 스타트 팀 점수
    start_sum = 0
    for i in range(len(start)):
        for j in range(len(start)):
            if i != j:
                start_sum += arr[start[i]][start[j]]

    # 링크 팀 점수
    link_sum = 0
    for i in range(len(link)):
        for j in range(len(link)):
            if i != j:
                link_sum += arr[link[i]][link[j]]

    # 3. 최솟값 갱신하기 !
    # 능력치 차의 최솟값 갱신
    diff = abs(start_sum - link_sum)
    if diff < min_diff:
        min_diff = diff
    return

# 입력
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')
recur(0, [])
print(min_diff)
