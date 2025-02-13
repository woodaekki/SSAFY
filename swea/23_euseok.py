import sys
sys.stdin = open("eusok.txt", "r")

def eusok():
    arr = []  
    cnt = 0   

    # 1. arr 5줄 입력받고, 길이값 구하기
    for _ in range(5):
        arr.append(input())  
        cnt += 1

    
    # 2. 가장 긴 길이의 리스트 찾기
    m = 0
    for num in arr:
        if len(num) > m:
            m = len(num) 

    lst = []  
    for j in range(m):  
        for i in range(5):  
            if j < len(arr[i]):  
                lst.append(arr[i][j])
            else:
                pass
    return ''.join(lst)

T = int(input())

for t in range(1, T + 1):
    print(f'#{t} {eusok()}')  