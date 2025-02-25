import sys
sys.stdin = open("calcu.txt", "r")

def calcu2(arr):


T = 10
for t in range(1, T + 1):
    n = int(input())  
    arr = list(input())  
    result = calcu2(arr)  
    print(f'#{t} {result}')