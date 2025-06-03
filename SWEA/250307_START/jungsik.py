def binary(two, three):
    two_lst = []
    for i in range(len(two)):
        new_two = list(two)
        for digit in '01':
            if new_two[i] != digit:
                new_two[i] = digit
            # 10진수로 바꾸기
            two_decimal = int("".join(new_two), 2)
            two_lst.append(two_decimal)
     
    three_lst = []
    for j in range(len(three)):
        new_three = list(three)
        for digit in '012':
            if new_three[j] != digit:
                new_three[j] = digit
        # 10진수로 바꾸기
            three_decimal = int("".join(new_three), 3)
            three_lst.append(three_decimal)
     
    # 교집합 구하기 
    common = 0
    for two in two_lst:
        if two in three_lst:
            common = two
    return common
     
T = int(input())
for t in range(1, T+1):
    two = input()
    three = input()
    result = binary(two, three)
    print(f'#{t} {result}')