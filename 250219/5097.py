import sys
sys.stdin = open("rotation.txt", "r")

def rotation(n,m,queue):
    cnt = 0 # 뒤로 보내는 작업 횟수
    while cnt != m:
        num = queue.pop(0)
        cnt += 1
        queue.append(num)
    return queue[0]

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    print(f'#{t} {rotation(n,m,queue)}')