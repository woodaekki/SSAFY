path = []
n = 3

# 주사위 3개 던져서 나올 수 있는 모든 조합
def run(cnt, start):
    if cnt == n:
        print(path)
        return

    for i in range(start,7):
        path.append(i)
        run(cnt+1, i)
        path.pop()

run(0, 1)