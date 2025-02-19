# < 선형 큐 >
# 1차원 배열의 큐

# front: 저장된 첫번째 원소의 인덱스
# rear: 저장된 마지막 원소의 인덱스

# 초기상태: front = rear = -1
# 공백상태: front == rear (= isEmpty())
# 포화상태: rear == n-1 (= isFull())

# 큐 생성
# queue = [0] * 3
# front = rear = -1
# #
# # 1, 2, 3 enqueue
# rear += 1
# queue[rear] = 1
#
# rear += 1
# queue[rear] = 2
#
# rear += 1
# queue[rear] = 3

# # deque
# front += 1
# print(queue[front])

# while front != rear:
#     front += 1
#     t = queue[front]
#     print(t)

# < 선형 큐의 문제점 >
# 원소의 삽입과 삭제를 계속할 경우, 앞부분에 활용할 수 있는 공간이 있음에도
# '포화상태' 로 인식하여 더이상의 삽입을 수행 x

# 해결: 매연산 수행할때마다 원소들을 배열의 앞쪽으로 이동시킴
# (시간의 비효율 문제 발생)

# 해결: '원형 큐'의 등장
# 초기상태: front = rear = 0

# 공백과 포화상태의 구분을 위해 front 자리는 항상 빈자리로 !

# mod n: 나머지 연산
# 큐에서 배열의 끝(n-1)에 도달하면 다시 맨 처음으로 돌아가도록

# 인큐하면, rear 가 한칸 뒤로 밀려나고, 원소가 채워짐
# 디큐하면, front 가 뒤로 한칸 밀려나고 항상 빈자리로 둬야하는 규칙에 따라 공백상태로

# 공백상태: front == rear (= isEmpty())
# 포화상태: (rear +1) % len(queue) == front (= isFull())
# -> 더이상 rear 가 밀려나지 못해서 front 와 같아지면 포화상태

