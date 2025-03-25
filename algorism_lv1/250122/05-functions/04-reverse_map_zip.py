# reverse
numbers = [1, 2, 3, 4, 5]
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]

# map
numbers = [1, 2, 3]
result = (map(str, numbers))
print(result) #<map object at 0x00000287DB85BFA0>
print(list(result))  # ['1', '2', '3']

# zip
girls = ['jane', 'ashley', 'happy']
boys = ['peter', 'jay']
pair = zip(girls, boys)
print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]
# => 두 변수의 개수가 다를 경우, 많은 쪽의 값은 무시


# zip 활용
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]
for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)

# * 활용
scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]
for score in zip(*scores):
    print(score)
