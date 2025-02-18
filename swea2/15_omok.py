import sys
sys.stdin = open("omok.txt", "r")

def check_omok():
    n = int(input())  # n x n 보드 크기 입력
    arr = []
    for _ in range(n):  # 보드 입력 받기
        arr.append(list(input()))

        for i in range(n):
            for j in range(n):
                # 가로 체크
                for k in range(5):
                    if j + k < n:
                        count = 0
                    if arr[i][j + k] == 'o':
                        count += 1
                if count == 5:
                    return "YES"

        # # 세로 체크
        # if i + 4 < n:
        #     count = 0
        #     for k in range(5):
        #         if arr[i + k][j] == 'o':
        #             count += 1
        #     if count == 5:
        #         return "YES"
        #
        # # 오른쪽 아래 대각선 (\) 체크
        # if i + 4 < n and j + 4 < n:
        #     count = 0
        #     for k in range(5):
        #         if arr[i + k][j + k] == 'o':
        #             count += 1
        #     if count == 5:
        #         return "YES"
        #
        # # 왼쪽 아래 대각선 (/) 체크
        # if i + 4 < n and j - 4 >= 0:
        #     count = 0
        #     for k in range(5):
        #         if arr[i + k][j - k] == 'o':
        #             count += 1
        #     if count == 5:
        #         return "YES"

# return "NO"
T = int(input())  # 테스트 케이스 개수 입력
for t in range(1, T + 1):
    result = check_omok()  # 오목 여부 확인
    print(f'#{t} {result}')  # 결과 출력