T = int(input())
for t in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    max_len = float('-inf')
 
    # 문자열 중 최대 길이
    for ar in arr:
        if len(ar) > max_len:
            max_len = len(ar)
 
    result = []
    for i in range(max_len):
        for j in range(5):
            if i < len(arr[j]):
                result.append(arr[j][i])
    print(f'#{t}', end=" ")
    for re in result:
        print(re, end='')
    print()