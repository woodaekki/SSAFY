import sys
sys.stdin = open("1.txt", "r")

def solve(n):
    wires = []  # 기존 선 저장
    cnt = 0  # 교차점 수
    # 새로운 선을 추가할때마다
    # (기존 선을 저장하면서)
    # 기존 선과 비교
    for _ in range(n):
        start, end = map(int, input().split())
        for prev_start, prev_end in wires:
            # 1. 새로운 선 시작점 > 기존 선 시작점 / 새로운 선 끝점 < 기존 선 시작점
            if start > prev_start and end < prev_end:
                cnt += 1
            # 2. 새로운 선 시작점 < 기존 선 시작점 / 새로운 선 끝점 > 기존 선 시작점
            if start < prev_start and end > prev_end:
                cnt += 1
        # 목록에 전선을 추가
        wires.append((start, end))
    return cnt

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    result = solve(n)
    print(f'#{t} {result}')
