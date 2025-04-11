import sys
sys.stdin = open("2.txt", "r")

tc = int(input())
T = int(input())
result = ""
for _ in range(T):
    arr = input().split()
    n = int(arr[1])
    result += arr[0] * n
print(result)
for i in range(len(result)//10):
    scope = result[0:i]
    print(scope)
