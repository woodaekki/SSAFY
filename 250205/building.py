# 빌딩 개수 10개 고정
# 기준 빌딩 인덱스 i의 i-2~ i+2로 빌딩 구간을 자른다. (범위 2부터 6까지)
# 기준빌딩이 가장 높은 건물이면 조망권 확보
# 그다음 높은 건물과의 높이 차이 구함.
# n번째 조망권까지 반복한다.

# import sys
# sys.stdin = open("sample_input.txt", "r")

T = 10
for t in range(1, T + 1):
    n = int(input()) # 건물의 개수
    arr = list(map(int, input().split())) # 건물 높이 리스트
    height = 0

    for i in range(2, n-2):
        lst = []  # 조망권 확보 건물 리스트
        scopes = arr[i-2:i+3] # 빌딩 구간 자르기
        standard = arr[i] # 기준 빌딩

        a = arr[i-2]
        b = arr[i-1]
        c = arr[i+1]
        d = arr[i+2]

        # 기준빌딩이 가장 높은 건물일때
        max_v = a

        if standard > a and standard > b and standard > c and standard > d:
            # 다른 4개의 빌딩 중 가장 높은 건물과의 차이
            if max_v <= b:
                max_v = b
            if max_v <= c:
                max_v = c
            if max_v <= d:
                max_v = d
            height += standard - max_v
    print(f'#{t} {height}')