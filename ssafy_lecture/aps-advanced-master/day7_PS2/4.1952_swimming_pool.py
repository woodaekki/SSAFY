import sys
sys.stdin = open("input.txt", "r")

# 완전 탐색을 하는 버전
# - 각 달에 4가지 케이스를 모두 확인하면서 진행
def recur(month, total_cost):
    global min_answer
    # 가지치기
    if min_answer < total_cost:
        return

    if month > 12:
        min_answer = min(min_answer, total_cost)
        return

    # 1일 이용권으로 다 사는 경우
    recur(month + 1, total_cost + (days[month] * cost_day))
    # 1달 이용권 사는 경우
    recur(month + 1, total_cost + cost_month)
    # 3달 이용권 사는 경우
    recur(month + 3, total_cost + cost_month3)
    # 1년 이용권 사는 경우
    recur(month + 12, total_cost + cost_year)


T = int(input())
for tc in range(1, T + 1):
    # 이용권 가격들 (1일, 1달, 3달, 1년)
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 12개월 이용 계획
    days = [0] + list(map(int, input().split()))
    min_answer = int(21e8)
    recur(1, 0)  # 1월부터 시작
    print(f'#{tc} {min_answer}')
