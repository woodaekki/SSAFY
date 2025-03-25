class Animal:    
    def __init__(self):
        pass
                
class Dog(Animal):
    def __init__(self):
        pass

    def bark(self):
        print('멍멍 !')
              
class Cat(Animal):
    def __init__(self, sound):
        self.sound = sound

    def meow(self):
        # 방법1. meow에 출력을 넣기
        print('야옹 !')


class Pet(Dog, Cat):
    # 클래스 변수
    def __init__(self, sound): # 인스턴스 변수
        self.sound = sound
    
    def play(self):
        print("애완동물과 놀기")
    
    def make_sound(self):
        print(f"{self.sound}")

    # 방법2. def meow 함수 만들어서 재정의하기
        

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()


