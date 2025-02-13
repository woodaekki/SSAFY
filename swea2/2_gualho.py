import sys
sys.stdin = open("g.txt", "r")

def pair():
    txt = input()
    stack = []

    for tx in txt:
        if tx == '(' or tx == '{':
            stack.append(tx)
        if tx == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                elif stack[-1] == '{':
                    return 0
            else:
                return 0

        if tx == '}':
            if stack:
                if stack[-1] == '{':
                    stack.pop()
                elif stack[-1] == '(':
                    return 0
            else:
                return 0

    if stack:
        return 0
    else:
        return 1

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {pair()}')