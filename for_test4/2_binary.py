import sys
sys.stdin = open("1.txt", "r")

# 소수의 이진수 변환 가능 여부 확인 위해서는
# -> 분모가 2의 거듭제곱인지 체크해야 함 

def binary(n):
    bin = ""
    cnt = 0 # 소수점 자리수 세기 
    
    while 0 < n < 1 and cnt < 12:
        n = n * 2
        if n >= 1:
            bin += "1"
            n -= 1
        else:
            bin += "0"
        cnt += 1 # 다음 소수점 자리수로 이동 
    
    if n > 0:
        return "overflow"
    return bin

T = int(input())
for t in range(1,T+1):
    n = float(input())
    result = binary(n)
    print(f'#{t} {result}')