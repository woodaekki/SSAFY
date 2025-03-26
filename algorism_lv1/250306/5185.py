import sys
sys.stdin = open("5185.txt","r")

def binary(n,hex):
    # 10진수를 2진수로 바꾸기
    remain = ""
    for ten in hex:
        # print(ten)
        # 2진수는 무조건 4자리이므로 몫이 0이 되건말건 무조건 4번을 돌아라
        for _ in range(4):
            remain = str(ten % 2) + remain
            ten = ten // 2
    # print(remain)
    # 4개씩 끊어서 앞으로 보내기
    ans = ""
    for i in range(0,len(remain),4):
        scope = remain[i:i+4]
        ans = scope + ans
    return ans


T = int(input())
for t in range(1, T + 1):
    dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    n, hex = input().split()

    n = int(n)
    hex = list(hex)
    # print(num)
    # 16진수를 10진수로 바꾸기
    for i in range(n):
        if hex[i].isdigit():
            hex[i] = int(hex[i])
        else:
            hex[i] = dic[hex[i]]
    # print(num)
    result = binary(n,hex)
    print(f'#{t} {result}')




