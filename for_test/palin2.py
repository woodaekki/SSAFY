import sys
sys.stdin = open("palin2.txt", "r")

def palin2():


# Process T test cases
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {palin2()}')