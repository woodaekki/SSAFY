import sys
sys.stdin = open("input.txt", "r")

def password():
    j = 0
    while True:
        num = queue.pop(0)
        j += 1
        queue.append(num - j)
        if num-j <= 0: # 0보다 작거나 같아지면
            queue.pop()
            queue.append(0) # 그 수는 0으로 저장
            break
        if j == 5: # 1사이클 다 돌때마다 j 초기화
            j = 0
 
    return queue
 
T = 10
for t in range(1, T+1):
    tc = int(input()) # 테스트 케이스 번호
    queue = list(map(int, input().split()))
    result = password()
    print(f'#{t} {result}')
