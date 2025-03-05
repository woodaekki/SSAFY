N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

CHILD_L = [0] * (N+1)
CHILD_R = [0] * (N+1)
PAR = [0] * (N+1)
lst = list(map(int, s.split()))
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    PAR[c] = p
    if not CHILD_L[p]:
        CHILD_L[p] = c
    else:
        CHILD_R[p] = c
print(CHILD_L)
print(CHILD_R)