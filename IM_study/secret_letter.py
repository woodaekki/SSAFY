import sys
sys.stdin = open("1.txt", "r")

def solve():
    for j in range(n - 1, -1, -1):
        for i in range(n):
            read = visited[i][j]
            print(read, end = "")

T = int(input())
for _ in range(T):
    arr = list(input())
    for i in range(1, len(arr)+1):
        if len(arr) // i == i:
            n = i
    visited = []
    for j in range(0, len(arr), n):
        scope = arr[j:j+n]
        visited.append(scope)

    solve()
    print()


