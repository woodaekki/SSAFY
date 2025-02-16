import sys
sys.stdin = open("count1.txt", "r")

def count1():
    n = int(input())
    arr = list(input())
    leng = 0
    max_leng = 0
    for i in range(n):
        if arr[i] == '1':
            leng += 1
        if arr[i] == '0':
            if leng > max_leng:
                max_leng = leng
            leng = 0
    # 끝까지 1인 경우
    if leng > max_leng:
        max_leng = leng
    return max_leng

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {count1()}')