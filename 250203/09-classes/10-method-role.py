class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
# 모든 메서드 호출할 수 있으나, 인스턴스 메서드만 사용하도록 함
# print(MyClass.instance_method(instance))
# print(MyClass.class_method())
# print(MyClass.static_method())


# 인스턴스가 할 수 있는 것
print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())
