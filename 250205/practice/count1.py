# 1. 입력받은 숫자가 1이라면 카운트 1증가
# 2. 그 다음 숫자가 1인 경우 카운트 증가 (if 안의 if문)
# 3. 그 다음 숫자가 0인 경우 반복문에서 빠져나오기

T = int(input())  

for t in range(1, T + 1):
    n = int(input())  # 수열의 길이
    arr = list(map(int, input().split()))  # 수열 입력 받기

    count = 0  
    i = 0

    while i < n:  # 수열의 끝을 넘지 않도록
        if arr[i] == 1:  # 숫자가 1일 경우
            count += 1  
            i += 1  

            # 그 다음 숫자가 1이면 카운트 증가
            if arr[i] == 1:  
                count += 1
                i += 1  # 그 다음 숫자 확인
        else:
            continue
        
        i += 1  # 1이 아닌 경우 빠져나와라
print(count) 



    
