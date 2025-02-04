# super()는 단순 직계 부모 클래스 상속이 아닌  mro 순서상 현재 클래스의 다음 클래스 호출
# 다중 상속
class ParentA:
    def __init__(self):
        super().__init__() # mro 'Child, ParentA, ParentB' 순서이므로 ParentB 호출
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # mro 'Child, ParentA, ParentB' 순서이므로 ParentA 호출
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')


child = Child()
child.show_value()
"""
Value from ParentA: ParentA
Value from Child: Child
"""

print(child.value_c) 
print(child.value_a)  
print(child.value_b)  


"""
1.1 Child 클래스의 인스턴스를 생성할 때 일어나는 일
    1.	child = Child() 호출 시, Child.__init__()가 실행
    2.	Child.__init__() 내부에서 super().__init__()를 호출
        - 여기서 Child의 super()는 MRO에 의해 ParentA의 __init__()를 가리킴
    3.	ParentA.__init__()로 진입

1.2. ParentA.__init__() 내부
	1.	ParentA.__init__()에는 다시 super().__init__()가 있음
	2.	ParentA를 기준으로 MRO에서 “다음 클래스”는 ParentB, 따라서 ParentA의 super().__init__()는 ParentB.__init__() 호출
    3.	ParentB.__init__()가 실행되면서 self.value_b = 'ParentB'가 설정됨
	4.	ParentB.__init__()가 종료된 후, 다시 ParentA.__init__()로 돌아와 self.value_a = 'ParentA'가 설정됨
	5.	ParentA.__init__() 종료 후, 다시 Child.__init__()로 돌아감
	6.	마지막으로 Child.__init__() 내에서 self.value_c = 'Child'가 설정되고 종료

1.3 결과적으로 child 인스턴스는 value_a, value_b, value_c 세 속성을 모두 갖게 됨
	- child.value_a → 'ParentA'
	- child.value_b → 'ParentB' 
	- child.value_c → 'Child'
"""
