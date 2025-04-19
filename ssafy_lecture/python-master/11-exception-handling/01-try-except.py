# try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')


# 복수 예외처리
try:
    num = int(input('숫자입력 : '))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('제대로 좀 입력해')


try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자를 입력하라고')
except ZeroDivisionError:
    print('0으로는 나눌 수 없어')
except:
    print('에러가 발생했습니다.')
