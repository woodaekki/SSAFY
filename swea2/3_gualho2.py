import sys
sys.stdin = open("g2.txt", "r")

def pair():
    n = int(input()) # s의 길이
    s = list(input())
    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        if c == ')':
            if not stack:
                return 0
            else:
                stack.pop()

    for c in s:
        if c == '[':
            stack.append(c)
        if c == ']':
            if not stack:
                return 0
            else:
                stack.pop()

    for c in s:
        if c == '{':
            stack.append(c)
        if c == '}':
            if not stack:
                return 0
            else:
                stack.pop()

    for c in s:
        if c == '<':
            stack.append(c)
        if c == '>':
            if not stack:
                return 0
            else:
                stack.pop()

    if stack:
        return 0
    else:
        return 1


T = 10
for t in range(1, T + 1):
    print(f'#{t} {pair()}')