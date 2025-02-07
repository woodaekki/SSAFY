import sys
sys.stdin = open("color.txt", "r")

T = int(input()) # 테스트 케이스 입력
for t in range(1, T+1):
    n = int(input())  # 칠할 영역의 개수
    arr = [[0] * 10 for _ in range(10)] # 빈 리스트 10x10로 초기화
    count = 0
    for _ in range(n): # 칠할 영역을 n줄 만큼 받는다.
        r1, c1, r2, c2, color = map(int, input().split()) #순서대로 r1 ~ color을 입력받는다.
        for i in range(r1, r2 + 1): #열과
            for j in range(c1, c2 + 1): #행을 순회하면서
                arr[i][j] += color # arr에 색을 칠함
                # 같은 영역에 같은 색을 칠하는 케이스는 없으므로
    # print(arr)
    for k in range(10):
        for l in range(10):
            if arr[k][l] == 3:
                count += 1
    print(f'#{t} {count}')
