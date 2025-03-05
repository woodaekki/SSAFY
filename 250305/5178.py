import sys
sys.stdin = open("5178.txt", "r")

T = int(input())
for t in range(1,T+1):
    n, m, l = list(map(int, input().split())) # 전체 노드수, 자식 수, 어떤 노드 번호에 저장된 값을 출력하고 싶은지
    tree = [0]*(n+1)
    for _ in range(m):
        node,value = list(map(int, input().split())) # 노드 번호, 저장된 값
        tree[node] = value
    # print(tree)
    for i in range(n,0,-1):
        if tree[i] == 0:
            if i*2 <=n and i*2+1<=n:
                tree[i] = tree[i*2] + tree[i*2+1]
            if i*2 <=n and i*2+1>n:
                tree[i] = tree[i*2]
    print(f'#{t} {tree[l]}')

