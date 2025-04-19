class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increse_population()

    @classmethod
    def increse_population(cls):
        cls.population += 1
    


person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  # 2

Person.increse_population()
print(Person.population)  # 3
