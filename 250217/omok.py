import sys
sys.stdin = open("omok.txt", "r")

# 발견한 순간 쭉 같은지 검사하기 
def omok():
    n = int(input())
    data = [list(input()) for _ in range(n)]

    # 가로줄 검사
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(5):
                if j + k < n and data[i][j] == 'o' and data[i][j] == data[i][j + k]:
                    cnt += 1
                else:
                    cnt = 0
                    break
                if cnt == 5:
                    return "YES"

    # 세로줄 검사
    for j in range(n):
        for i in range(n):
            cnt = 0
            for k in range(5):
                if i + k < n and data[i][j] == 'o' and data[i][j] == data[i + k][j]:
                    cnt += 1
                else:
                    cnt = 0
                    break
                if cnt == 5:
                    return "YES"

    # 왼쪽에서 오른쪽으로 가는 대각선
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(5):
                if i + k < n and j + k < n and data[i][j] == 'o' and data[i][j] == data[i + k][j + k]:
                    cnt += 1
                else:
                    cnt = 0
                    break
                if cnt == 5:
                    return "YES"

    # 오른쪽에서 왼쪽으로 가는 대각선
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(5):
                if i + k < n and j - k >= 0 and data[i][j] == 'o' and data[i][j] == data[i + k][j - k]:
                    cnt += 1
                else:
                    cnt = 0
                    break
                if cnt == 5:
                    return "YES"

    return "NO"

 
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {omok()}')
    