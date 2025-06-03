# 해당 숫자에서 갈 수 있다면 1을 기록한다.
# 연속된 1의 길이가 가장 긴곳이 정답이다.
# 같은 길이가 있다면, 작은 수가 정답 위치
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n*n+1) # 1번부터 시작
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    # 현재 위치 숫자 기준 상하좌우 확인
    # 1 큰곳이 있다면 visited 기록
    for i in range(n):
        for j in range(n):
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == arr[i][j]+1:
                    # 현재 숫자는 다음으로 이동이 가능하다.
                    visited[arr[i][j]] = 1
                    break # 나머지 방향은 볼 필요가 없다.
    # print(visited)
 
    # 연속된 1의 개수가 가장 긴 곳을 찾는다.
    # 가장 긴 길이, 현재 몇 개인지, 출발지
    max_cnt = cnt = start = 0
    for i in range(1, n*n+1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt
            cnt = 0
    print(f'#{t} {start} {max_cnt+1}')