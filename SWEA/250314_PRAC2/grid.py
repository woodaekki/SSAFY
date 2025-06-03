def recur(i, j, number):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    if len(number) == 7:
        result.add(number)
        return
 
    for di, dj in directions:
        ni = i + di
        nj = j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            # 다음 위치 추가하면서 진행
            recur(ni, nj, number+matrix[ni][nj])
 
# 재귀(상하좌우 이동)로 숫자를 이어 붙인다.
# 숫자가 7자리가 되면, set에 넣는다. (중복 제거)
T = int(input())
for t in range(1, T+1):
    matrix = [input().split() for _ in range(4)]
    result = set()
 
    for i in range(4):
        for j in range(4):
            recur(i, j, matrix[i][j])
    # print(result)
    print(f'#{t} {len(result)}')