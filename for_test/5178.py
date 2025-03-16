import sys
sys.stdin = open("1.txt", "r")

def node_sum(node):
    
    
T = int(input())
for t in range(1, T+1):
    n, m, l = list(map(int, input().split()))

    for _ in range(m):
        node, value = list(map(int, input().split()))
       
    result = node_sum(1)
    print(f'#{t} {result}')
        