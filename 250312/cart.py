import sys
sys.stdin = open("6.txt", "r")

def recur(k, mid):
    global result
    # 중간에 더한 값이 이전 저장해둔 값보다 크면 끝내라.
    if mid > result:
        return

    # k는 트리의 깊이
    if k == n:
        # 마지막 구간에서 사무실로 돌아가는 값 추가하기
        result = min(result, mid+arr[path[-1]][0])
        return

    # if k == n:
    #     # print(path)
    #     sumv = 0
    #     for i in range(n-1):
    #         start = path[i]
    #         end = path[i+1]
    #         value = arr[start][end]
    #         sumv += value
    #     # 마지막 구간에서 사무실로 돌아가는 소모량
    #     sumv += arr[path[-1]][0]
    #     result = min(result, sumv)
    #     return

    for i in range(n):
        if not used[i]:
            used[i] = True
            path.append(i)
            recur(k+1, mid+arr[path[-2]][i])
            path.pop()
            used[i] = False

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    path = []
    used = [False] * n
    result = 100*n*n
    path.append(0) # 미리 0 넣고 가기
    used[0] = True
    # recur(1) # 그 후 1번 부터 시작하기
    recur(1, 0)
    print(f'#{t} {result}')