import sys
sys.stdin = open("password.txt","r")

code_dict = {
(3, 2, 1, 1) : 0,
(2, 2, 2, 1) : 1,
(2, 1, 2, 2) : 2,
(1, 4, 1, 1) : 3,
(1, 1, 3, 2) : 4,
(1, 2, 3, 1) : 5,
(1, 1, 1, 4) : 6,
(1, 3, 1, 2) : 7,
(1, 2, 1, 3) : 8,
(3, 1, 1, 2) : 9,
}

def password():
    # 2진수로 된 코드 찾기 
    for i in range(n):  
        for j in range(m - 1, 54, -1): 
            # 1찾기
            if arr[i][j] == 1:  # 뒤에서 코드 끝점인 1 찾기
                code = []
                for _ in range(8): # 
                    c1, c2, c3, c4 = 0, 0, 0, 0 # 1, 0, 1, 0 몇개씩 있는지 세기 
                    while arr[i][j] == 1:  # 1의 개수세기
                        c4 += 1
                        j -= 1
                    while arr[i][j] == 0:  # 0의 개수세기
                        c3 += 1
                        j -= 1
                    while arr[i][j] == 1:  # 1의 개수세기
                        c2 += 1
                        j -= 1
                    # 남은 길이를 계산하여 첫 번째 구간 개수 결정
                    c1 = 7 - c2 - c3 - c4
                    j -= c1 # 다음 숫자 읽어야되니까 앞으로 땡기기 
                    # print(code_dict[(c1, c2, c3, c4)], end=' ')
                    code.append(code_dict[(c1, c2, c3, c4)])
                
                odd_sum = code[1] + code[3] + code[5] +code[7]
                even_sum = code[0] + code[2] + code[4] +code[6]
                # 코드 유효성: 홀수 자리 합 * 3 + 짝수 자리 합이 10의 배수인지 확인
                if (odd_sum * 3 + even_sum) % 10 == 0:  
                    return odd_sum + even_sum
                return 0
   
T = int(input())  
for t in range(1, T + 1):
    n,m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    result = password()
    print(f'#{t} {result}')