import sys
sys.stdin = open("1.txt", "r")

def solve():
    counting = [0] * len(A)
    for j in range(len(B)):
        for i in range(len(A)):
            if A[i] <= B[j]:
                counting[i] += 1
                break
    max_vote = float('-inf')
    num = []
    for j in range(len(A)):
        if counting[j] > max_vote:
            max_vote = counting[j]
            num.append(j)
    # return num[-1] + 1 # 1번부터 시작
    return counting
T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = solve()
    print(f'#{t} {result}')

