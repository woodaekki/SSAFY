import sys
sys.stdin = open("switch.txt", 'r')

def switch():
    n = int(input()) # 스위치 개수 
    a, b = [list(map(int, input().split())) for _ in range(2)] # 조작전, 조작후 
    cnt = 0 # 스위치 조작 횟수 

    for i in range(0, n):
        if a[i] != b[i]:
            cnt += 1 # 다를때 마다 바꿔야하니까 횟수 1증가가
            for j in range(i, n): # i번부터 n번까지 조작
                if a[j] == 1:
                    a[j] = 0
                else:
                    a[j] = 1
    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {switch()}')