# import sys
# sys.stdin = open("gap.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    max_idx = 0  
    min_idx = 0  

    for i in range(1, n):  # 첫 번째 값을 제외한 나머지 값을 탐색
        # 최대값의 위치는 마지막에 나오는 최대값의 인덱스를 찾기
        if arr[max_idx] <= arr[i]:
            max_idx = i
        
        # 최소값의 위치는 첫 번째에 나오는 최소값의 인덱스를 찾기
        if arr[min_idx] > arr[i]:
            min_idx = i

    max_idx += 1
    min_idx += 1

    # 둘의 차이가 음수일 경우, 절댓값 씌우기 
    diff = max_idx - min_idx
    if diff < 0:
        diff = -diff
    print(f'#{t} {diff}')