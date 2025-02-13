import sys
sys.stdin = open("p.txt", "r")

def palin():
    n, m = list(map(int, input().split()))
    arr = [input() for _ in range(n)]

    mv = 0
    for ar in arr:
        for i in range(len(ar)//2):
            if ar[i] == ar[i-1]:
                s = len(ar)
                if s > mv:
                    mv = s
    return mv

print(f'가장 긴 팰린드롬의 길이: {palin()}')