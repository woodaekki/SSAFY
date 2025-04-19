items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)

country = 'Korea'

for char in country:
    print(char)


my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])


numbers = [4, 6, 10, -8, 5]

for idx in range(len(numbers)):
    numbers[idx] = numbers[idx] * 2

print(numbers)  # [8, 12, 20, -16, 10]


outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)
"""
A c
A d
B c
B d
"""


elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)  # ['A', 'B'] ['c', 'd']

for elem in elements:
    for item in elem:
        print(item)  # A B c d
