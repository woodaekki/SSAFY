class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population()
    
    @classmethod # 클래스 메서드, 첫번째 인자로 메서드 호출
    def increase_population(cls):
        cls.population += 1

person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  

