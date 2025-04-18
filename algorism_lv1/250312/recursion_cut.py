import sys
sys.stdin = open("5.txt", "r")

def recur(row, col, mid):
    global result

    # 이미 저장해 둔 result 보다 이미 합의 크기가 넘어버리면 끝내라.
    if mid > result:
        return

    # 도착하면 좌표의 최소합 구하기
    if row == n-1 and col == n-1:
        # print(path)
        # sumv = 0
        # for row, col, value in path:
        #     sumv += value
        result = min(result, mid)
        return

    # 아래로
    if 0 <= row < n-1:
        # path.append((row+1, col, arr[row+1][col]))
        recur(row + 1, col, mid+arr[row+1][col])
        # path.pop()
    # 위로
    if 0 <= col < n-1:
        # path.append((row, col+1, arr[row][col+1]))
        recur(row, col+1, mid+arr[row][col+1])
        # path.pop()

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # path = [(0, 0, arr[0][0])]
    result = 10*n*n
    recur(0, 0, arr[0][0])
    print(f'#{t} {result}')