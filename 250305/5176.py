import sys
sys.stdin = open("5176.txt", "r")

def midtree(node):
    global num
    if node > n:  # n보다 커지면 탐색할 노드가 없으므로 종료
        return
    midtree(node * 2)  # 왼쪽 자식 노드를 먼저 탐색
    tree[node] = num  # 부모 노드에 num 값을 저장
    num += 1  # num을 1 증가시켜 다음 노드에 할당
    midtree(node * 2 + 1)  # 오른쪽 자식 노드를 탐색

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    tree = [0] * (n + 1)
    num = 1
    midtree(1)
    # print(tree)
    print(f'#{t} {tree[1]} {tree[n//2]}')

