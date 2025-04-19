class Animal:
    def eat(self):
        print('먹는 중')


class Dog(Animal):
    def bark(self):
        print('멍멍')

# 인스턴스 생성
my_dog = Dog()

# 인스턴스 메서드 호출
my_dog.bark()  # 멍멍

# 부모 클래스(Animal) 메서드 사용 가능
my_dog.eat()  # 먹는 중
