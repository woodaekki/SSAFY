# 퍼펙트 셔플
def get_result():
    a = 0
    b = (len(arr) + 1) // 2

    for turn in range(len(arr)):
        if turn % 2 == 0:
            print(arr[a], end = ' ')
            a += 1
        else:
            print(arr[b], end = ' ')
            b += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().split())
    print(f'#{tc} ', end = '') # end 옵션 줄바꿈 안되게
    get_result()
    print()