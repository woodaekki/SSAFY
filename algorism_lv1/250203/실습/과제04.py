class Person:
    number_of_people = 0

    def __init__(self, name, age): # init은 Person
        self.name = name
        self.age = age
        

    def introduce(self):
        print(f"제 이름은 {self.name}이고, 저는 {self.age} 살 입니다.") # person n마다 자신의 속성을 소개해야함
        Person.number_of_people += 1 


person1 = Person("Alice", 25)
person1.introduce() # person1은 introduce 함수를 부름

print(Person.number_of_people)
