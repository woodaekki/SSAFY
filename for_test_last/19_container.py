import sys
sys.stdin = open("1.txt", "r")

def solve():
    i = j = result = 0
    while m > i and n > j:
        if truck[i] >= container[j]:
            result += container[j]
            i += 1
            j += 1
        else:
            j += 1
    return result

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container = sorted(container, reverse=True)
    truck = sorted(truck, reverse=True)
    result = solve()
    print(f'#{t} {result}')


