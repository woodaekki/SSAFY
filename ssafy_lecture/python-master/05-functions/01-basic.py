def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2


result = make_sum(100, 30)
print(result)  # 130

# print() 함수는 반환값이 없다.
return_value = print(1)
print(return_value)  # None


def my_func():
    print('hello')


result = my_func()
print(result)  # None
