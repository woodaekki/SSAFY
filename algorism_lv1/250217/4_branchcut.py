def powerset(k, curS):
    global result

    # 누적합이 이미 10이 되어버린 경우 끝까지 갈 필요가 없음
    # 가지를 치자.
    if curS > 10:
        return

    if curS == 10:
        print(result, curS)
        return

    if k == n:
        return

    result[k] = 1
    powerset(k+1, curS+arr[k])
    result[k] = 0
    powerset(k + 1, curS)

n = 5
arr = [1, 12, 3, 4, 5]
result = [-1] * n
powerset(0, 0)
