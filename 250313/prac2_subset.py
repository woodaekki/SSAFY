arr = ['A', 'B', 'C', 'D', 'E']
path = []

# 5명 중 3명을 뽑을 수 있는 모든 경우
n = 3
def run(lev, start):
    if lev == n:
        print(path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        run(lev+1, i+1)
        path.pop()

run(0, 0)