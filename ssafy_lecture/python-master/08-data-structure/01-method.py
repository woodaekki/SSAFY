print(type('1'))  # <class 'str'>
print(type([1, 2])) # <class 'list'>
print(help(str))



# 클래스 파트에서 이어서 진행 할 예정!
def add(a, b):
    return a + b

class Calculator:
    def add(self, a, b):
        return a + b

# 함수 호출
add(1, 2)

# 메서드 호출
a = Calculator()
a.add(1, 2)
