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

n = int(input())
arr = list(map(int, input().split()))

left = [0] * (n+1)
right = [0] * (n+1)

for i in range(0, len(arr), 2):
    parent = arr[i]
    child = arr[i+1]
    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent] = child 

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