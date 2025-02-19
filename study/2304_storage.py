def storage():
    arr = [0]*1001
    max_y = max_x = -999999

    n = int(input())
    for _ in range(n):
        x, y = list(map(int, input().split()))
        arr[x] = y # 형식 저장

        # 기둥의 최대 높이, 인덱스 구하기
        if y > max_y:
            max_y = y
            max_x = x
    
    # 최대 기둥 좌측
    # 기둥이 최대 기둥 높이를 넘기전까지 누적합
    leftv = 0
    left_max = 0
    for i in range(max_x + 1):  
        if arr[i] > left_max:  
            left_max = arr[i]
        leftv += left_max  

    # 최대 기둥 우측
    rightv = 0
    right_max = 0
    for j in range(1000, max_x, -1):  
        if arr[j] > right_max:  
            right_max = arr[j]
        rightv += right_max 

    return leftv + rightv

print(storage())