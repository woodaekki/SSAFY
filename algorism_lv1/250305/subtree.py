import sys
sys.stdin = open("5174.txt", "r")

def midtree(node):
    global cnt
    if node: # 노드가 있으면
        cnt += 1 # 불렀으니 카운트 1 증가
        midtree(left[node]) # 왼쪽 자식 노드 탐색하고
        midtree(right[node]) # 오른쪽 자식 노드 탐색함
    return cnt

T = int(input())
for t in range(1, T+1):
    e, n = list(map(int, input().split())) # 간선 수, 루트 노드
    arr = list(map(int, input().split()))
    left = [0] * (e+2)
    right = [0] * (e+2)
    tree = [0] * (n+1)
    for i in range(e):
        l = arr[i*2]
        r = arr[i*2+1]
        # 트리 생성하기
        if left[l] == 0: # 왼쪽 노드가 없으면
            left[l] = r # 오른쪽 값 채우고
        else: # 있으면
            right[l] = r # 오른쪽 노드에 오른쪽 값 정상적으로 채우기
    cnt = 0  # 루트 노드를 부르는 횟수 = 서브트리 노드 개수
    result = midtree(n) # 루트노드부터 시작
    print(f'#{t} {result}')


