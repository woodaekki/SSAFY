import sys
sys.stdin = open("tree.txt", "r")

def preorder(node):
    if node == 0:
        return
    result1.append(node)
    preorder(left[node])
    preorder(right[node])

def inorder(node):
    if node == 0:
        return
    inorder(left[node])
    result2.append(node)
    inorder(right[node])

def postorder(node):
    if node == 0:
        return
    postorder(left[node])
    postorder(right[node])
    result3.append(node)

"""
가로로 제시된 부모-자식 노드 
"""
v = int(input())  # 트리의 정점 수 입력
arr = list(map(int, input().split()))  # 부모-자식 관계 입력

left = [0] * (v + 1)  # 왼쪽 자식 노드를 저장하는 배열
right = [0] * (v + 1)  # 오른쪽 자식 노드를 저장하는 배열

# 트리 생성하기
for i in range(0, len(arr), 2):
    parent = arr[i]  # 부모 노드
    child = arr[i + 1]  # 자식 노드

    if left[parent] == 0:  # 왼쪽 자식이 없으면
        left[parent] = child  # 왼쪽 자식에 자식 노드 할당
    else:  # 왼쪽 자식이 이미 있으면
        right[parent] = child  # 오른쪽 자식에 자식 노드 할당

result1 = []
preorder(1)
for re1 in result1:
    print(re1, end = " ")
print()

result2 = []
inorder(1)
for re2 in result2:
    print(re2, end = " ")
print()

result3 = []
postorder(1)
for re3 in result3:
    print(re3, end = " ")