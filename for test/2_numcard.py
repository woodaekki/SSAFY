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
    max_value = -9999999
    for key, value in dict.items():
        if value > max_value:
            max_key = int(key)
            max_value = value
        # 카드 장수가 동일한 경우 적힌 숫자가 큰 쪽
        if value == max_value:
            if int(key) > max_key:
                max_key = int(key)
            else:
                pass

    return max_key, max_value

T = int(input())
for t in range(1, T+1):
    n = int(input()) # 카드 장수
    arr = list(input())
    result = numcard()
    print(f'#{t} {result[0]} {result[1]}')
