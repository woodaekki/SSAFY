def calcu():
    num_lst = []
    mix_lst = []
 
    # 후위 표기식 만들기
    for i in range(n):
        if arr[i].isdigit():
            num_lst.append(int(arr[i]))
            mix_lst.append(arr[i])
        elif arr[i] == '+':
            mix_lst.append(arr[i])
 
    for j in range(n):
        if mix_lst[j] == '+':
            a = num_lst.pop()
            b = num_lst.pop()
            num_lst.append(a+b)
    return num_lst[0]
 
 
T = 10
for t in range(1, T+1):
    n = int(input())
    arr = list(input())
    print(f'#{t} {calcu()}')