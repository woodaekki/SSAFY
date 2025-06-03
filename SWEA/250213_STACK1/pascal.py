def pascal():
    n = int(input())
    ans = []
    ans.append([1])
    for i in range(1, n):
        lst = []
        for j in range(0, i+1):
            if j == 0:
                lst.append(1)
            elif j == i:
                lst.append(1)
            else:
                lst.append(ans[i-1][j-1] + ans[i-1][j])
        ans.append(lst)
 
    return ans
 
T = int(input())
for t in range(1, T+1):
    print(f'#{t}')
    pa = pascal()
    for i in pa:
        print(*i, sep = " ")