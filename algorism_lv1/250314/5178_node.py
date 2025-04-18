import sys
sys.stdin = open("rooted.txt", "r")

def postorder(node):
    if node > n:
        return
    postorder(node*2)
    postorder(node*2+1)

    if node * 2 <= n:
        tree[node] += tree[node * 2]
    if node * 2 + 1 <= n:
        tree[node] += tree[node * 2 + 1]
    return tree[l]
    

# 세로로
# 노드 - 노드 안의 값
T = int(input())
for t in range(1, T+1):
    n, m, l = list(map(int, input().split()))
    tree = [0] * (n+1)
    for _ in range(m):
        node, value = list(map(int, input().split()))
        tree[node] = value
    
    result = postorder(1)
    print(f'#{t} {result}')