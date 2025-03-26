'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장
right = [0]*(N+1)       #
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장

# 루트 노드 찾기
root = 1
for i in range(1, N+1):
    if par[i] == 0:
        root = i
        break
print(root)

# 트리 구조 저장하기
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:          # 왼쪽자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p # 부모 노드 저장

# 전위 순회하기
def pre_order(T):
    if T:
        print(T, end = " ")
        pre_order(left[T])
        pre_order(right[T])

# 중위 순회하기
def in_order(T):
    if T:
        in_order(left[T])
        print(T, end = " ")
        in_order(right[T])

# 후위 순회하기
def post_order(T):
    if T:
        post_order(left[T])
        post_order(right[T])
        print(T, end = " ")

pre_order(root)
# print()
# in_order(root)
# print()
# post_order(root)