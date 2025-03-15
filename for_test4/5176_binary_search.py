import sys
sys.stdin = open("tree.txt", "r")

def inorder(node):
    global value
    if node > n:
        return
    inorder(node*2)
    tree[node] = value
    value += 1
    inorder(node*2+1)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)
    value = 1
    inorder(1)
    print(f'#{t} {tree[1]} {tree[n//2]}')