# 일반적인 함수 
def addition(x, y):
    return x + y
result = addition(3, 5)
print(result)  # 8

# lambda로 변환
addition = lambda x, y: x + y
result = addition(3, 5)
print(result)