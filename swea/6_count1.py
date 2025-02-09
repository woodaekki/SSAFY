# 1. 입력받은 숫자가 1이라면 카운트 1증가
# 2. 그 다음 숫자가 1인 경우 카운트 증가 (if 안의 if문)
# 3. 그 다음 숫자가 0인 경우 반복문에서 빠져나오기
import sys
sys.stdin = open("count1.txt", "r")

T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input()))
    
    cnt = 0  # 현재 연속된 1의 개수 저장
    max_cnt = 0
    for i in range(n):
        if arr[i] == 1:
            cnt += 1  # 1이면 증가
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 0  # 0을 만나면 초기화
    print(f'#{t} {max_cnt}')

    






    
