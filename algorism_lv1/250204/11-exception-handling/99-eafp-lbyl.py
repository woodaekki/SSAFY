my_dict = {'key': 'value'}

# EAFP (Easier to Ask for Forgiveness than Permission, 허락보다 용서 구하기)
# 예외 발생 후 처리 중심
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')


# LBYL (Look Before You Leap, 돌다리도 두들겨보고 건너기)
# 예외 전 미리 값 검사 중심
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
