# 클래스 메서드가 필요한 이유
# "자식 클래스에서 부모 클래스의 클래스 메서드 호출하기"
# ---------------------------------------
# 1. 클래스 메서드의 장점
#   - 인스턴스 생성 없이 클래스 속성(total_count, dog_count, cat_count)에 접근할 수 있다.
#   - 상속 계층에서 부모 클래스의 클래스 메서드를 자식 클래스가 쉽게 사용하면서, 자식 클래스에 맞는 로직(예: dog_count, cat_count)도 추가로 처리 가능하다.
# 	2.	cls 키워드의 의미
# 	- 메서드가 속한 현재 클래스를 가리킨다. (인스턴스 메서드에서는 self가 인스턴스를 가리키는 것과 유사)
# 	- cls 덕분에 자식 클래스에서 부모 클래스의 코드를 재사용하거나, 자식 클래스만의 로직을 구현하기가 쉬워진다.
# 	3.	상속과 클래스 메서드
# 	- 자식 클래스에서 cls를 사용하면, 현재 호출된 클래스 타입에 따라 클래스 속성을 관리할 수 있다. (예: Dog.dog_count, Cat.cat_count)
# 	- 또한 부모 클래스의 메서드(get_total_count)도 재사용 가능하므로, 중복 코드를 줄이고 유지보수를 쉽게 할 수 있다.

# 이처럼 클래스 메서드는 클래스 레벨의 데이터 관리나 상속 시 부모 메서드의 재사용이 필요할 때 매우 유용하다.
# ---------------------------------------


class Animal:
    total_count = 0  # 모든 동물의 총 개수 (클래스 속성)

    def __init__(self, name):
        self.name = name
        Animal.total_count += 1  # 인스턴스 생성 시 전체 동물 수를 1 증가

    @classmethod
    def get_total_count(cls):
        """
        모든 Animal(및 자식 클래스 포함)의 인스턴스 수를 반환하는 클래스 메서드.
        클래스 속성인 total_count에 직접 접근 가능하며,
        cls 키워드를 통해 어떤 클래스에서 호출해도 해당 클래스의 네임스페이스를 사용하게 됨.
        """
        return f'전체 동물 수: {cls.total_count}'


class Dog(Animal):
    dog_count = 0  # Dog 클래스만의 강아지 개수 (클래스 속성)

    def __init__(self, name, breed):
        super().__init__(
            name
        )  # 부모 클래스(Animal)의 __init__으로 total_count 관리
        self.breed = breed
        Dog.dog_count += 1  # 강아지 인스턴스 생성 시 dog_count 1 증가

    @classmethod
    def get_dog_info(cls):
        """
        Dog 클래스의 클래스 메서드.
        - cls.get_total_count(): 부모 클래스(Animal)의 클래스 메서드 호출
          -> 전체 동물 수(Animal.total_count) 확인
        - cls.dog_count: Dog 클래스의 클래그 속성
          -> 전체 강아지 수 확인
        """
        return f'{cls.get_total_count()}, 강아지 수: {cls.dog_count}'


class Cat(Animal):
    cat_count = 0  # Cat 클래스만의 고양이 개수 (클래스 속성)

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        Cat.cat_count += 1  # 고양이 인스턴스 생성 시 cat_count 1 증가

    @classmethod
    def get_cat_info(cls):
        """
        Cat 클래스의 클래스 메서드.
        - cls.get_total_count(): 부모 클래스(Animal)의 클래스 메서드 호출
          -> 전체 동물 수(Animal.total_count) 확인
        - cls.cat_count: Cat 클래스의 클래스 속성
          -> 전체 고양이 수 확인
        """
        return f'{cls.get_total_count()}, 고양이 수: {cls.cat_count}'


# ---------------------------------------
# 인스턴스 생성 및 메서드 호출 예시
# ---------------------------------------
dog1 = Dog('멍멍이', '삽살개')
dog2 = Dog('바둑이', '진돗개')
print(Dog.get_dog_info())
# 출력 예: 전체 동물 수: 2, 강아지 수: 2
# -> Dog 클래스의 get_dog_info() 내부에서 Animal의 get_total_count()를 호출,
#    그리고 Dog 클래스의 dog_count에 접근해 정보를 한꺼번에 제공


cat1 = Cat('노아', '페르시안')
cat2 = Cat('루비', '코숏')
print(Cat.get_cat_info())
# 출력 예: 전체 동물 수: 4, 고양이 수: 2
# -> Cat 클래스의 get_cat_info() 내부에서 Animal의 get_total_count()를 호출,
#    그리고 Cat 클래스의 cat_count에 접근해 정보를 한꺼번에 제공
