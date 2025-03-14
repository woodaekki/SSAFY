import sys
sys.stdin = open("rooted.txt", "r")

def tree_sum(tree):
    for i in range(n, 0, -1): # 1번 노드
        if tree[i] == 0:
            if i * 2 <= n and i * 2 + 1 <= n:
                tree[i] = tree[i * 2] + tree[i * 2 + 1]
            if i * 2 <= n and i * 2 + 1 > n:
                tree[i] = tree[i * 2]
    return tree[l]

# 세로로
# 노드 - 노드 안의 값
T = int(input())
for t in range(1, T+1):
    n, m, l = list(map(int, input().split())) # 노드 개수, 자식 노드, 값
    tree = [0]*(n+1)
    for _ in range(m):
        node, value = list(map(int, input().split()))
        tree[node] = value
    print(f'#{t} {tree_sum(tree)}')
