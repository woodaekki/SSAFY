# N = 13
# s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
#
# TREE = [[] for _ in range(N+1)]
# lst = list(map(int, s.split()))
# for i in range(0, len(lst), 2):
#     p = lst[i]
#     c = lst[i+1]
#     TREE[p].append(c)
#
# print(TREE)
#
# def pre_order(root):
#     print(root)
#     if len(TREE[root]) > 0: #왼쪽트리가 있으면:
#         pre_order(TREE[root][0])
#     if len(TREE[root]) > 1:
#         pre_order(TREE[root][1])
#
# pre_order(1)
#
# print('==========')
# def in_order(root):
#     if len(TREE[root]) > 0: #왼쪽트리가 있으면:
#         in_order(TREE[root][0])
#     print(root)
#     if len(TREE[root]) > 1:
#         in_order(TREE[root][1])
#
# in_order(1)

# N = 13
# s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
#
# TREE = [[0, 0] for _ in range(N+1)]
# lst = list(map(int, s.split()))
# for i in range(0, len(lst), 2):
#     p = lst[i]
#     c = lst[i+1]
#     if TREE[p][0]:  #왼쪽에 데이터가 있으면
#         TREE[p][1] = c
#     else:
#         TREE[p][0] = c
#
# print(TREE)
#
# def pre_order1(root):
#     print(root)
#     if TREE[root][0]:
#         pre_order(TREE[root][0])
#     if TREE[root][1]:
#         pre_order(TREE[root][1])
#
#
# def pre_order(T):
#     if T:
#         print(T)
#         pre_order(TREE[T][0])
#         pre_order(TREE[T][1])
#
# def post_order(T):
#     if T:
#         post_order(TREE[T][0])
#         post_order(TREE[T][1])
#         print(T)
#
# pre_order(1)
# print('=======')
# post_order(1)


def pre_order(root_idx):
    if root_idx <= N:
        print(TREE[root_idx])
        pre_order(root_idx*2)
        pre_order(root_idx*2 + 1)

def in_order(root_idx):
    if root_idx <= N:
        in_order(root_idx*2)
        print(TREE[root_idx])
        in_order(root_idx*2+1)

def in_order(root_idx):
    if root_idx*2 <= N:
        in_order(root_idx * 2)
    print(TREE[root_idx])
    if root_idx*2+1 <= N:
        in_order(root_idx * 2)

N = 10
TREE = [0] * (N+1)
for i in range(10):
    TREE[i+1] = chr(ord('A') + i)
print(TREE)

pre_order(1)