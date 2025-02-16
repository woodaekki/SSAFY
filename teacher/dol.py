T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    # 1차원 델타배열
    dx = [-1, 1] # 왼쪽, 오른쪽
    for _ in range(M):
        center, K = map(int, input().split())
        # 인덱스를 0부터 시작으로 조정
        center -= 1
        for j in range(1, K + 1):
            left = center + dx[0] * j
            right = center + dx[1] * j
            # 범위체크
            if left < 0 or right >= N: continue
            if stones[left] == stones[right]:
                # 뒤집기
                stones[left] = 1 - stones[left]
                stones[right] = 1 - stones[right]

    print(f'#{tc}', *stones)