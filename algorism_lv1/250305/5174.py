import sys
sys.stdin = open("5174.txt", "r")

def tree(node):
    global cnt
    if node: # 루트 노드가 있으면
        cnt += 1
        tree(left[node]) #왼쪽
        tree(right[node]) #오른쪽
    return cnt

T = int(input())
for t in range(1, T+1):
    e, n = list(map(int, input().split())) # 간선 수, 루트 노드
    left = [0] * (e + 2)
    right = [0] * (e + 2)
    arr = list(map(int, input().split()))
    for i in range(e):
        l = arr[2*i]
        r = arr[2*i+1]
        if left[l] == 0: # 왼쪽 노드가 없을때
            left[l] = r # 왼쪽 노드에 오른쪽 값을 넣음
        else: # 왼쪽 노드가 있을때
            right[l] = r # 오른쪽 노드에 오른쪽 값 넣음
    cnt = 0
    result = tree(n) # 루트 노트를 부를때마다
    print(f'#{t} {result}')

