import sys
sys.stdin = open("1.txt", "r")

def solve():
    pass




T = int(input())
for t in range(1, T+1):
    n, m, k = list(map(int, input().split())) # 배터리량, 종점 번호, 충전소 수
    stop = list(map(int, input().split())) # 충전기 설치된 정류장 번호
    result = solve()
    print(f'#{t} {result}')