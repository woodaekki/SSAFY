num = 0  # 전역 변수

def increment(): #매개변수()안의 변수 - global 변수와 달라야함 
    global num  # num를 전역 변수로 선언
    num += 1

print(num)  # 0
increment() # 호출
print(num)  # 1
increment() # 호출
print(num) # 2