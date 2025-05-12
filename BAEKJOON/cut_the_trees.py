import sys
sys.stdin = open("1.txt", "r")

def solve():
    cutting = arr[-1]
    new_arr = []
    for i in range(n):
        new_arr.append(arr[i] - cutting)
        sumv = 0
        for j in range(n):
            if new_arr[j] > 0:
                sumv += new_arr[j]
        if sumv > m:
            return cutting
        else:
            cutting -= 1



n, m = list(map(int, input().split())) # 나무의 수, 나무의 길이
arr = list(map(int, input().split()))
arr.sort()
solve()
# print(result)