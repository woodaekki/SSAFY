import sys
sys.stdin = open("2.txt", "r")

def solve(arr):
    max_leng = 0 
    for i in range(n):  
        cnt = 0  
        curr = arr[i]  
        for j in range(i+1, n): 
            if arr[j] > curr:
                # print(curr, arr[j])
                cnt += 1  
                curr = arr[j]  
                # print(curr)
        max_leng = max(max_leng, cnt) 
    return max_leng

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve(arr)
    print(f'#{t} {result}')