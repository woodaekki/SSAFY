def decto(value, bit):
    # 149 => '149'
    # 149 => 149//10 => 14, 9 # 10진수는 15까지 존재
    # 14 => 14//10 => 1, 4
    # 1 => 1//10 => 0, 1 # 나머지를 거꾸로 나열한 정수를 문자열로 바꾸기(16진수)
    result = ''
    while value:
        remain = value % bit
        value = value // bit
        # print(value, remain)
        if remain < 10:
            result = str(remain) + result
        else:
            # mapp = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
            # result = mapp[remain] + result
            result = chr(ord('A') + (remain-10)) + result
    return result

print(decto(149, 10)) # 10진수로 바꾸기
print(decto(22, 2)) # 2진수로 바꾸기
print(decto(171, 16)) # 16진수로 바꾸기

def todec(s, bit):
    #149 => ((1*10) + 4)*10) + 9
    value = 0
    for c in s:
        if c.isdigit():
            value = (value*bit) + int(c)
        else:
            #'A', 'B' ~ 'F'
            # mapp = {'A':10, 'B':11, 'C':12, 'D':13,'E':14, 'F':15}
            # value = (value * bit) + mapp[c]
            value = (value*bit) + ord(c)-ord('A')+10
    return value

value = '149'
print(todec(value, 10))
value = '110110'
print(todec(value, 2))
value = 'AB'
print(todec(value, 16))
