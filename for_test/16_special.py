import sys
sys.stdin = open("C:/Users/dora0/Desktop/ssafy/Learned/for_test/special.txt", "r")


def special():
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        
    for k in range(n//2, n-1):
        for l in range(k+1, n):
            if arr[k] < arr[l]:
                arr[k], arr[l] = arr[l], arr[k]
    
    for i in range(n//2):
        front = arr[0:i+1]
        back = arr[i+1:n+1]
    
    file = list(zip(back,front))

    return file
    

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = special()
    print(f'#{t}', end = " ")
    for re in result:
        print(f'{re[0]} {re[1]}', end = " ")
    print("", sep=" ")

    