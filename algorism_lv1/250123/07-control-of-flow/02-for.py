#1
items = ['apple', 'banana', 'coconut']

for item in items:
    print(items)

#2
country = 'Korea'

for char in country:
    print(char)

#3
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])

#4
numbers = [4, 6, 10, -8, 5]

for idx in range(len(numbers)):
    numbers[idx] = numbers[idx] * 2
print(numbers)  


#5
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner) #안쪽 반복문은 outers 리스트의 각 항목에 대해 1번씩 실행

#6
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)  # ['A', 'B'] ['c', 'd']

for elem in elements:
    for item in elem:
        print(item)  # A B c d
