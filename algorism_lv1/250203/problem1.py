def min_score(score):
    min_val = 99999
    for s in score:
        if s < min_val:
            min_val = s
    return min_val

print(min_score([1, 100, 3, 4, 200, 1000]))