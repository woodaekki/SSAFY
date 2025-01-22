# 1. packing
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)

numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers # 변수 앞의 *는 리스트형으로 출력 !!
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

def my_func(*args): # 매개변수 앞의 *은 튜플형으로 출력 !!
    print(args)  
my_func(1, 2, 3, 4, 5) # (1, 2, 3, 4, 5)

# 2. unpacking
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5

def my_function(x, y, z):
    print(x, y, z)
names = ['alice', 'jane', 'peter']
my_function(*names)  # *를 호출할때 사용하면 풀어서 -> alice jane peter

def my_function(x, y, z):
    print(x, y, z)
my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # **를 호출할때 사용하면 풀어서 -> 1 2 3