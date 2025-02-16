import sys
sys.stdin = open("numcard.txt", "r")

def numcard():
    dict = {}
    for num in arr:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    
    max_key = -9999999
    max_value = -99999999
    for key, value in dict.items():
        if value > max_value:
            max_value = value
            max_key = key
        # 카드 장수가 같을 때는 큰 수 출력
        if max_value == value:
            if key > max_key:
                max_key = key
    return max_key, max_value

    
T = int(input())
for t in range(1, T+1):
    n = int(input()) # 카드 장수
    arr = list(input())
    result = numcard()
    print(f'#{t} {result[0]} {result[1]}')
