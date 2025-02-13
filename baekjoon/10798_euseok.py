def eusok():
    arr = [list(input()) for _ in range(5)]

    # 최대 가로 길이
    k = 0
    for ar in arr:
        if len(ar) > k:
            k = len(ar)

    new = []
    for j in range(k):
        for i in range(5):
            if j < len(arr[i]):
                new.append(arr[i][j])
            else:
                pass
    return "".join(new)

result = eusok()
print(result)