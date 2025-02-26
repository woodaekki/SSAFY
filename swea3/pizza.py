import sys
sys.stdin = open("pizza.txt", "r")

def pizza(cheezes):
    oven = []


T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    cheezes = list(map(int, input().split()))
    result = pizza(cheezes)
    print(f'{result}')
