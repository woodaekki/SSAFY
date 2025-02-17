T = int(input())

def solve():
    n = int(input())
    ar = [list(map(str, input())) for _ in range(10)]
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 방향

    for i in range(10): # 행
        for j in range(10): # 열
            monster = ar[i][j]
            if monster == '1' or monster == '2' or monster == '3': # 현재위치가 몬스터일때 조명 색 지정
                if monster == '1':
                    light = 'R'
                elif monster == '2':
                    light = 'G'
                elif monster == '3':
                    light = 'B'

                for k in direct: # 4방향

                    for h in range(1, int(monster)+1): # 몬스터가 빛을 쏘는 범위

                        dy, dx = i + k[0]*h, j + k[1]*h



                        if 0 <= dy < 10 and 0 <= dx < 10 :
                            if ar[dy][dx] == '1' or ar[dy][dx] == '2' or ar[dy][dx] == '3' or ar[dy][dx] == '4':
                                break  # 벽이나 몬스터만나면 더 이상 그 방향으로 빛을 쏘지 않음
                            ar[dy][dx] = light  # 벽이나 몬스터가 아니면 빛 쏘기

    count = 0
    for i in range(10):
        for j in range(10):
            if ar[i][j] == '0': # 안전구역인지 확인 후 카운트 증가
                count +=1
    return count

for t in range(1, T+1):
    print(f'#{t} {solve()}')