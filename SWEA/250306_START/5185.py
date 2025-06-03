def binary(n, sixteen):
    dicts = {"A": '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
    for i in range(n):
        for key, val in dicts.items():
            if sixteen[i] == key:
                sixteen[i] = val
    # print(sixteen)
    # 2진수로 만들기
    for j in range(n):
        value = int(sixteen[j])
        remained = ""
        # print(value)
        while value > 0:
            remain = value % 2
            remained = str(remain) + remained
            value = value // 2
        # print(remained)
        # 0채우기
        remained = remained.zfill(4)
        ans.append(remained)
    return "".join(ans)
 
 
T = int(input())
for t in range(1, T+1):
    n, sixteen = list(map(str, input().split()))
    n = int(n)
    sixteen = list(sixteen)
    ans = []
    # print(sixteen)
    result = binary(n, sixteen)
    print(f'#{t} {result}')