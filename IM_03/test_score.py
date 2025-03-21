import sys
sys.stdin = open("test.txt", "r")  # 디버깅 시 주석 처리 가능

<<<<<<< HEAD
def solve(n, arr):
    scores = [0]
    for ar in arr:
        new_scores = set()
        for score in scores:
            new_scores.add(score+ar)
        scores.extend(new_scores)
    return set(scores)
=======
def solve(n, arr):  # n과 arr을 매개변수로 추가

>>>>>>> 23e7101cf876ede5c3d42dfb9d8dceff634ed6f0

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
<<<<<<< HEAD
    result = solve(n, arr)
    print(f'#{t} {len(result)}')


=======
    result = solve(n, arr)  # n과 arr을 전달
    print(result)
>>>>>>> 23e7101cf876ede5c3d42dfb9d8dceff634ed6f0
