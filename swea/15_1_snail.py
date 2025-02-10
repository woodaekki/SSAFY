# 달팽이 배열을 만드는 함수
def create_snail(N):
    # N x N 크기의 배열 초기화
    snail = [[0] * N for _ in range(N)]
    
    # 초기 위치 설정
    num = 1
    x, y = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위
    dir_idx = 0  # 현재 방향 인덱스 (0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위)
    
    while num <= N * N:
        snail[x][y] = num
        num += 1
        
        # 다음 칸으로 이동
        next_x = x + directions[dir_idx][0]
        next_y = y + directions[dir_idx][1]
        
        # 이동할 곳이 배열의 범위를 벗어나거나 이미 숫자가 있다면 방향을 바꿈
        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N or snail[next_x][next_y] != 0:
            dir_idx = (dir_idx + 1) % 4  # 방향을 시계방향으로 전환
            next_x = x + directions[dir_idx][0]
            next_y = y + directions[dir_idx][1]
        
        x, y = next_x, next_y
    
    return snail

# 테스트 케이스 처리
T = int(input())  # 테스트 케이스 수 입력

for t in range(1, T + 1):
    N = int(input())  # N 입력
    snail = create_snail(N)
    
    print(f"#{t}")
    for row in snail:
        print(" ".join(map(str, row)))
