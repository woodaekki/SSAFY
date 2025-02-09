# 1. 문자열을 입력받는다. 
# 2. 아스키코드로 변환한다.
# 3. 연속한 숫자로 나오는지 확인한다
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input()) # 테스트 케이스 입력

for t in range(1, T+1):
    arr = input() # 문자열 입력받기
    count = 0
    if arr[0] == 'a': # 첫번째 인덱스가 a 일때
        count = 1 # 카운트 1증가
        for i in range(0, len(arr)-1): # 인덱스 에러 조심 !!
            if ord(arr[i]) + 1 == ord(arr[i+1]):
                count += 1
            else:
                break
    else:
        count = 0
    print(f'#{t} {count}')