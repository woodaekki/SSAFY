import sys
sys.stdin = open("fly.txt", "r")

# m x m 파리채 구간을 만든다
# n x n 배열을 돌며 m x m 구간의 누적합을 만든다.
# 한 구간이 끝나면 누적합은 달리 만들어놓은 maxv와 비교하여 크면 maxv = 누적합이 되고
# 누적합은 0으로 갱신되며 다른 m x m 구간 합을 또 만든다.

T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    n, m = list(map(int, input().split()))  # n x n 배열, m x m 파리채
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))  # 배열 입력받기

    maxv = 0  # 최대 파리합 저장
    for n1 in range(n - m + 1):  # n x n 배열
        for n2 in range(n - m + 1):  # n-m까지 인덱스 에러 주의 !
            fly = 0  # 파리 누적합
            for f1 in range(n1, n1 + m):  # m x m 파리채
                for f2 in range(n2, n2 + m):
                    fly += arr[f1][f2]  # 0,1/0,2/1,0/2,0 구간 합
            if fly > maxv:
                maxv = fly  # 최대값 갱신
    print(f'#{t} {maxv}')


                


        
    


