class Animal:
    num_of_animal = 0
    

    def __init__(self):
        Animal.num_of_animal += 1
                

class Dog(Animal):
    def __init__(self):
        super().__init__() # Animal 호출


class Cat(Animal):
    def __init__(self):
        super().__init__() # Animal 호출


class Pet(Dog, Cat):
    def __init__(self):
        super().__init__()
        

    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal} 마리 입니다.'
    


dog = Dog() # Animal.num_of_animal += 1
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())

