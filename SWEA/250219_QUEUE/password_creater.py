def password():
    i = 0
    while True:
        i += 1
        t = queue.pop(0)
        if t-i <= 0:
            queue.append(0)
            break
        else:
            queue.append(t-i)
        # 한 사이클 종료시, i 초기화 
        if i == 5:
            i = 0
    return queue
 
T = 10
for t in range(1, T+1):
    tc = int(input()) # 테스트 케이스 번호
    queue = list(map(int, input().split()))
    result = password()
    print(f'#{t}', end = " ")
    print(*result)