import sys
sys.stdin = open("jungsik.txt", "r")

def bank():
    # 2진수
    two_lst = [0, 1]
    copy_two = two.copy()
    for i in range(len(two)):
        for two_l in two_lst:
            if copy_two[i] != two_l: #1010
                copy_two[i] = two_l # 0010
                print(copy_two)
                # 다시 1010으로




T = int(input())
for t in range(1,T+1):
    two = list(map(int, input()))
    three = list(map(int, input()))
    result = bank()
    print(f'#{t} {result}')

