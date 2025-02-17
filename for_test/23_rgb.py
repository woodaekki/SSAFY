T = int(input())

def rgb():
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(10):
        for j in range(10):
            sumv = arr[i][j]
            if sumv == '1' or sumv == '2' or sumv == '3' or sumv == '4':
                break
            for di, dj in directions:
                for step in range(1, arr[i][j]+1):
                    ni, nj = i+di*step, j+dj*step

                        if sumv == '1':
                            light = 'r'
                        if sumv == '2':
                            light = 'g'
                        if sumv == '3':
                            light = 'b'
                        if sumv == '4':
                            light


#     for i in range(10): # 행
#         for j in range(10): # 열
#             monster = ar[i][j]
#             if monster == '1' or monster == '2' or monster == '3': # 현재위치가 몬스터일때 조명 색 지정
#                 if monster == '1':
#                     light = 'R'
#                 elif monster == '2':
#                     light = 'G'
#                 elif monster == '3':
#                     light = 'B'
#
#                 for k in direct: # 4방향
#
#                     for h in range(1, int(monster)+1): # 몬스터가 빛을 쏘는 범위
#
#                         dy, dx = i + k[0]*h, j + k[1]*h
#
#
#
#                         if 0 <= dy < 10 and 0 <= dx < 10 :
#                             if ar[dy][dx] == '1' or ar[dy][dx] == '2' or ar[dy][dx] == '3' or ar[dy][dx] == '4':
#                                 break  # 벽이나 몬스터만나면 더 이상 그 방향으로 빛을 쏘지 않음
#                             ar[dy][dx] = light  # 벽이나 몬스터가 아니면 빛 쏘기
#
#     count = 0
#     for i in range(10):
#         for j in range(10):
#             if ar[i][j] == '0': # 안전구역인지 확인 후 카운트 증가
#                 count +=1
#     return count
#
# for t in range(1, T+1):
#     print(f'#{t} {solve()}')