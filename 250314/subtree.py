import sys
sys.stdin = open("sub.txt", "r")

def subtree(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    subtree(left[node])
    subtree(right[node])
    return cnt

"""
가로로 부모-자식 노드
"""
T = int(input())
for t in range(1, T+1):
    e, root = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    left = [0] * (e+2)
    right = [0] * (e+2)
    for i in range(0, len(arr), 2):
        parent = arr[i]
        child = arr[i+1]
        if left[parent] == 0: # 왼쪽 없으면
            left[parent] = child
        else:
            right[parent] = child

    cnt = 0
    result = subtree(root)
    print(f'#{t} {result}')