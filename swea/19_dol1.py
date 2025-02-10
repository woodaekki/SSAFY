import sys
sys.stdin = open("dol.txt", "r")

def rock():
    n, m = list(map(int, input().split())) # 돌의 총 개수, i, j 몇 번 전환할지 줄 수
    arr = list(map(int, input().split())) # 돌의 초기 상태 
    for _ in range(0, m):
        i, j = map(int, input().split()) # i번째부터 j개의 돌을 i번째 돌의 색을 교체
        
        # 1. 바꿀 돌의 범위 설정하기 
        scope = arr[i-1 : i+j-1]

        # 2. scope 내의 모든 수를 i(scope인덱스의 0번째 수)로 바꿔라 
        for k in range(i-1, i+j-1):
            if k < n:
                arr[k] = scope[0]
    return arr

T = int(input())
for t in range(1, T+1):
    result = rock()
    print(f'#{t}', end = " ")
    for dol in result:
        print(f'{dol}', end = " ")
    print()