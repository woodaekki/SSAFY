import sys
sys.stdin = open("tree.txt", "r")

def bank(two, three):
    # 2진수 가능 리스트 
    change_twolst = []
    for i in range(len(two)):
        new_two = list(two)  
        for digit in '01':
            if new_two[i] != digit:
                new_two[i] = digit
        two_decimal = int("".join(new_two), 2)  # 2진수를 십진수로
        change_twolst.append(two_decimal)
    
    # 3진수 가능 리스트 
    change_threelst = []
    for i in range(len(three)):
        new_three = list(three)  
        for digit in '012':
            if new_three[i] != digit:
                new_three[i] = digit
                three_decimal = int("".join(new_three), 3)  # 3진수를 십진수로
                change_threelst.append(three_decimal)

    # 교집합 찾기
    common = 0
    for num in change_twolst:
        if num in change_threelst:
            common = num
    return common

T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    two = input()
    three = input()
    result = bank(two, three) 
    print(f'#{t} {result}')