import sys
sys.stdin = open("1.txt", "r")

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        ar = input().split()
        alpha = ar[0]
        num = int(ar[1])
        arr.append(alpha * num)
    lst = "".join(arr)
    # print(lst)
    print(f'#{t}')
    for i in range(0, len(lst), 10):
        scope = lst[i:i+10]
        print(scope)



