import sys
sys.stdin = open("switch.txt", "r")

def switch():
    cnt = 0
    for i in range(0, n):
        while before[i] != after[i]:
            for j in range(i, n):
                if before[j] == 1:
                    before[j] = 0
                else:
                    before[j] = 1
            cnt += 1
    return cnt    
                
T = int(input())
for t in range(1, T+1):
    n = int(input()) # 가로줄 길이 
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))
    print(f'#{t} {switch()}')