# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom): # '상속 순서: 아빠, 엄마'
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry())  # 
print(baby1.swim())  # 
print(baby1.walk())  # -> 아기의 부모클래스인 아빠에게서 상속 활용
# < 다이아몬드 문제 >
print(baby1.gene)  # 부모 클래스 모두에게 있는 '중복 속성'의 경우 '상속 순서'에 의해 결정
