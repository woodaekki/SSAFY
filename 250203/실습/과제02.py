class StringRepeater:
    def repeat_string(self, num, alpha):
        for _ in range(0, num):
            print(alpha)

repeater1 = StringRepeater() # 괄호 안에 없으면 class 함수 내부의(인스턴스 함수 등) 재료를 사용
#하지만 괄호안에 있으면 __init__ 만들어서 받아줘야함 
repeater1.repeat_string(3, "Hello")
