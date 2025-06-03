def subtree(node):
    global cnt
    if node == 0:
        return
     
    subtree(left[node])
    subtree(right[node])
    cnt += 1
    return cnt 
 
T = int(input())
for t in range(1, T+1):
    e, root = list(map(int, input().split()))
    arr = list(map(int, input().split()))
 
    left = [0] * (e+2)
    right = [0] * (e+2)
    for i in range(0, len(arr), 2):
        parent = arr[i]
        child = arr[i+1]
 
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child
     
    cnt = 0
    result = subtree(root)
    print(f'#{t} {result}')