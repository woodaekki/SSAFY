import sys
sys.stdin = open("2.txt", "r")

while True:
    try:
        arr = input()
        print(arr)
    except EOFError:
        break
