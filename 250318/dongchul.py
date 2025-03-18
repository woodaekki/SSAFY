import sys
sys.stdin = open("chul.txt", "r")

def recur(row, success_rate):
    global max_success
    # 가지치기, 0~1 사이의 숫자이므로 곱할 수록 값이 작아질 확률 높음
    # 현재 확률이 이미 최댓값보다 낮다면 반환 
    if success_rate <= max_success:  
        return
    
    if row == n:
        # print(work)
        max_success = max(max_success, success_rate)
        return
    
    # 일 조합 만들기
    for person in range(n):
        if visited[person]:
            continue
       
        visited[person] = 1
        recur(row+1, success_rate * arr[row][person])
        visited[person] = 0

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr[i][j] / 100 # 확률로 저장하기 
    
    work = [0] * n
    visited = [0] * n
    max_success = float('-inf')
    recur(0, 1)
    print(f'#{t} {max_success*100:.6f}') # 소수점 6자리 까지