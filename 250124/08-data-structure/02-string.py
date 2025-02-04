# find
text = 'banana'
print(text.find('k')) # 문자가 없다면 -1 
print(text.find('a'))

# index: 가장 먼저 등장한 문자의 인덱스 1개만 출력
print(text.index('a')) 
# print(text.index('z'))  # 문자가 없다면 오류 

# isupper: 전부 대문자인지 여부 확인 
# is로 시작하는 메서드는 bool 타입으로 출력 !
string1 = 'HELLO'
string2 = 'hello'
print(string1.isupper())  
print(string2.isupper())  

# islower: 전부 소문자인지 여부 확인 
print(string1.islower())  
print(string2.islower())  

# isalpha: 전부 알파벳으로만 이루어져있는지 여부 확인 
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  
print(string2.isalpha())  


# replace
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)
print(new_text1)  
print(new_text2)  # Hello, Python! world world: 바꿀 문자열의 위치 지정
print(text) # 문자열은 불변이므로 원본 변화 x

# strip
text = '  Hello, world!  '
new_text = text.strip() # 공백 제거 
print(new_text)

# split
# sep: 구분자 문자열
text = 'Hello, world!'
words1 = text.split(',') # ,을 기준으로 나눔
words2 = text.split() # 공백 기준으로 나눔
print(words1)  # ['Hello', ' world!']
print(words2)  # ['Hello,', 'world!']


# join
words = ['Hello', 'world!']
new_text = ''.join(words)
print(new_text)  # Hello-world!

# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# title
new_text2 = text.title()
print(new_text2)  # Hello, World!

# upper
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4)  # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!


# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal())
print("'-123'.isdecimal():", '-123'.isdecimal())
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())
