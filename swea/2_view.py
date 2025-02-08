import sys
sys.stdin = open("view.txt", "r") 

T = 9
for t in range(1, T + 1):
    n = int(input()) # 건물의 개수
    arr = list(map(int, input().split())) # 건물 높이 리스트
    height = 0
 
    for i in range(2, n-2):
        scopes = arr[i-2:i+3] # 빌딩 구간 자르기
        standard = arr[i] # 기준 빌딩
 
        a = arr[i-2]
        b = arr[i-1]
        c = arr[i+1]
        d = arr[i+2]
 
        # 기준빌딩이 가장 높은 건물일때
        max_v = a
 
        if standard > a and standard > b and standard > c and standard > d:
            # 다른 4개의 빌딩 중 가장 높은 빌딩
            if max_v <= b:
                max_v = b
            if max_v <= c:
                max_v = c
            if max_v <= d:
                max_v = d
            # 기준빌딩과 max_v의 차이 = 조망권 획득 세대
            height += standard - max_v
    print(f'#{t} {height}')