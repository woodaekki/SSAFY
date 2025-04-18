# cnt = 재귀호출마다 누적되어서 전달되어야 하는 값
def recur(x, sum):
    global cnt
    if sum > 10:
        return

    if x == 3:
        cnt += 1
        return

    # 주사위는 1부터 6까지
    for i in range(1, 7):
        path.append(i)
        recur(x+1, sum+i)
        path.pop()

cnt = 0 # 10 이하일 때 카운트 저장
path = [] # 뽑은 카드를 저장
recur(0, 0)
print(cnt)