
def powerset(k, curS):

    # if 의미없으면:
    #     return
    if curS > 10:
        return

    if curS == 10:
        print(result, curS)
        return

    if k==N:
        return

    result[k] = 1
    powerset(k+1, curS+arr[k])
    result[k] = 0
    powerset(k+1, curS)


def per_1(k):
    if k==N:
        print(result)
        return

    candidates = []
    for i in range(N):
        if i not in result[0:k]:
            candidates.append(i)

    for i in candidates:
        result[k] = i
        per(k+1)

def per(k):
    if k==N:
        print(result)
        return


    for i in range(N):
        if not visited[i]:
            result[k] = i
            visited[i] = True
            per(k+1)
            visited[i] = False

N = 3
arr = [1, 12, 3, 4, 5]

result = [-1] * N

# powerset(0, 0)
visited = [False] * N
per(0)