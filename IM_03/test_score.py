import sys
sys.stdin = open("test.txt", "r")  # 디버깅 시 주석 처리 가능

def solve(n, arr):
    scores = [0]
    for ar in arr:
        new_scores = set()
        for score in scores:
            new_scores.add(score+ar)
        scores.extend(new_scores)
    return set(scores)

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve(n, arr)
    print(f'#{t} {len(result)}')