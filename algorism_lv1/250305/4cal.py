import sys
sys.stdin = open("4cal.txt","r")

T = 1
for t in range(1,T+1):
    n = int(input())
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    value = [0] * (n + 1)
    for _ in range(n):
        arr = list(map(str, input().split()))
        # p, p_cal, l, r (p, p번에 들어갈 연산자, p의 왼쪽 자식, p의 오른쪽 자식
        if len(arr) == 4:
            p = int(arr[0])
            p_cal = arr[1]
            l = int(arr[2])
            r = int(arr[3])
            value[p] = p_cal
            left[p] = l  # 왼쪽 자식 번호 저장
            right[p] = r
        if len(arr) == 3:
            p = int(arr[0])
            p_cal = arr[1]
            l = int(arr[2])
            r = 0
        if len(arr) == 2:
            p = int(arr[0])
            p_cal = arr[1]
            l = 0
            r = 0
        # print(p,p_cal,l,r)
        print(left,right,value)