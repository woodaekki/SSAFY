import sys
sys.stdin = open("color.txt", "r")

def coloring():
    arr = [[0] * 10 for _ in range(10)] # 빈 리스트 생성
    cnt = 0
    n = int(input()) # 몇줄 받을 건지 

    for _ in range(n):
        r1, r2, c1, c2, color = list(map(int, input().split())) 

        # 빨강, 파랑 칠하기
        for i in range(r1, c1+1):
            for j in range(r2, c2+1):
                if color == 1:
                    arr[i][j] += 1
                elif color == 2:
                    arr[i][j] += 2
        
    # 보라 칸 세기
    for k in range(10):
        for l in range(10):
            if arr[k][l] == 3:
                cnt += 1

    return cnt
    
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {coloring()}')