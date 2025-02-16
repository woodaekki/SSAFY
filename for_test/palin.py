import sys
sys.stdin = open("palin.txt", "r")

def palin():
    arr = list(input())
    cnt = 0

    # 문자열의 길이값 
    for ar in arr:
        cnt += 1
    
    for i in range(cnt):
        if arr[i] == arr[-1-i]:
            return 1
        else:
            return 0

                
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {palin()}')