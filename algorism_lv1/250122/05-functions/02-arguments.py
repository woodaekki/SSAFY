# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
greet('Alice', 25)  
# greet('Alice') # => {name}, {age} 2개이므로, 입력해야 할 인자 개수 또한 2개


# 2. Default Argument Values
def greet(name, age=20): #age = 20으로 기본 인자값 정의 
    print(f'안녕하세요, {name}님! {age}살이시군요.')
greet('Bob') # => 인자 개수가 1개일 경우, 자동 기본 인자값으로 출력 


# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
greet(age=35, name='Dave') #-> 키워드를 지정해주면 자동으로 순서를 변경


# 4. Arbitrary Argument Lists
def calculate_sum(*args): # *: 정해지지 않은 개수의 키워드 인자 튜플로 처리
    print(args)  
calculate_sum(1, 100, 5000, 30) 


# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs): # **: 정해지지 않은 개수의 키워드 딕셔너리 형태로 처리
    print(kwargs)
print_info(name='Eve', age=30)  


# 1~5 적용 !!!
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)

func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
# pos1: 1
# pos2: 2
# default_arg: 3
# args: (4, 5, 6)
# kwargs: {'key1': 'value1', 'key2': 'value2'}

