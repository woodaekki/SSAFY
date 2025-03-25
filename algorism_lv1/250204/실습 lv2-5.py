class Dog:
    sound = "멍멍"
    def __init__(self):
        pass


class Cat:
    sound = '냐옹'
    def __init__(self):
        pass

# dog Class를 우선 상속하였을 경우
class Pet(Dog, Cat):
    @classmethod
    def __str__(cls):
        return f'애완동물은 {cls.sound} 소리를 냅니다.'

# # cat Class를 우선 상속하였을 경우
# class Pet(Cat, Dog):
#     @classmethod
#     def __str__(cls):
#         return f'애완동물은 {cls.sound} 소리를 냅니다.'
    
pet = Pet()
print(pet)