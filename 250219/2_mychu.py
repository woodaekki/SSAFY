# -----새로 들어온 애는 무조건 1개------
# -----나갔다가 들어올때, 1개씩 추가-----
from collections import deque

queue = deque()
new_mychu = 1
total = 0 # 마이쮸 총 개수
while total < 20:
    queue.append((new_mychu, 1)) # 새로 들어온 마이쮸 번호, 개수
    new_mychu += 1
    # print(new_mychu)
    # print(queue)
    mychu, cnt = queue.popleft() # 나갔다가
    total += cnt
    print(f'{mychu}번이 {cnt}개 가져감 -> 총 {total}개')
    queue.append((mychu, cnt + 1)) # 들어올때 1개씩 추가
    # print(queue)

print(mychu)
