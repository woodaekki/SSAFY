import sys
sys.stdin = open("1.txt", "r")

def binary():
    dict = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
    binary_lst = []
    for i in range(n):
        if sixteen[i] in dict:
            sixteen[i] = dict[sixteen[i]]
            # print(sixteen[i])
    for six in sixteen:
        remained = ""
        value = int(six)
        while value > 0:
            remain = int(value) % 2
            remained = str(remain) + remained
            value = int(value) // 2
        # print(remained)
        # 0 채우기 
        remained = remained.zfill(4)
        binary_lst.append(remained)
    return "".join(binary_lst)

T = int(input())
for t in range(1,T+1):
    n, m = list(map(str, input().split()))
    n = int(n)
    sixteen = list(m)
    result = binary()
    print(f'#{t} {result}')   
