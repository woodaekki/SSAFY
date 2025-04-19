# 5명 중 3명을 뽑는 조합 문제
arr = ['A', 'B', 'C', 'D', 'E']
n = 3

path = []

# 5명 중 3명을 뽑는 문제
def recur(cnt, start):
    # N명을 뽑으면 종료
    if cnt == n:
        print(*path)
        return

    # for i in range(이전에 뽑았던 인덱스 + 1부터, len(arr)):
    # start : 이전 재귀로부터 넘겨받아야 하는 값
    for i in range(start, len(arr)):
        path.append(arr[i])
        # i: i번째를 뽑겠다.
        # i + 1을 매개변수로 전달: 다음 재귀 부터는 i+1 부터 고려
        recur(cnt + 1, i + 1)
        path.pop()


recur(0, 0)

