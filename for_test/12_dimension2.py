import sys
sys.stdin = open("dimension2.txt", "r")

def dimension2():
    n = int(input()) # 테스트 케이스 번호 
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    max1 = max2 = max3 = -999999999999
    # 가로
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
            if total >= max1:
                max1 = total
    
    # 세로
    for j in range(100):
        total2 = 0
        for i in range(100):
            total2 += arr[i][j]
            if total2 >= max2:
                max2 = total2

    # 대각선
    for i in range(100):
        total3 = 0
        for j in range(100):
            total3 += arr[i][i]
            total3 += arr[i][j-1]
        total3 -= arr[100//2][100//2]
        if total3 >= max3:
            max3 = total
    
    if max1 >= max2 and max1 >= max3:
        return max1
    if max2 >= max3 and max2 >= max1:
        return max2
    if max3 >= max1 and max3 >= max2:
        return max3
        
T = 10
for t in range(1, T+1):
    print(f'#{t} {dimension2()}')