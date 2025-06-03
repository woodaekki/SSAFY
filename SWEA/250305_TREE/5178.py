def node_sum(node):
    if node > n:
        return
     
    node_sum(node*2)
    node_sum(node*2+1)
 
    if node*2 <= n:
        tree[node] += tree[node*2]
    if node*2+1 <= n:
        tree[node] += tree[node*2+1]
    return tree[l]
     
T = int(input())
for t in range(1, T+1):
    n, m, l = list(map(int, input().split()))
 
    tree = [0] * (n+1)
    for _ in range(m):
        node, value = list(map(int, input().split()))
        tree[node] = value
        
    result = node_sum(1)
    print(f'#{t} {result}')