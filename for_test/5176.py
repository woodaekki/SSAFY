import sys
sys.stdin = open("1.txt", "r")

def binary(node):
    global value
    if node > n:
        return
    
    binary(node*2)
    tree[node] = value
    value += 1
    binary(node*2+1)
    return tree


T = int(input())
for t in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)
    value = 1
    binary(1)
    print(f'#{t} {tree[1]} {tree[n//2]}')