# 오버라이딩
class Animal:
    def eat(self):
        print('Animal이 먹는 중')


class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 '재정의')
    
    def eat(self):
        print('Dog가 먹는 중')


my_dog = Dog()

my_dog.eat()  
