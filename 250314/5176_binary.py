import sys
sys.stdin = open("0.txt", "r")

def preorder(node):
    global cnt
    if node > n:
        return 
    preorder(node*2)
    tree[node] = cnt
    cnt += 1
    preorder(node*2+1)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    cnt = 1
    tree = [0] * (n+1)
    preorder(1)
    # 루트, n//2번 노드
    print(f'#{t} {tree[1]} {tree[n//2]}')