# Scope 예시
def func():
    num = 20
    print('local', num)  
print(func()) # return이 없으므로 자동 None 처리

# LEGB Rule 퀴즈
a, b = 1, 2
def enclosed():
    a, c = 10, 3
    def local(c): 
        print(a, b, c)  
    local(500) 
    print(a, b, c)  

enclosed() #호출: 10 2 500 / #10 2 3
print(a, b)  # 1 2
