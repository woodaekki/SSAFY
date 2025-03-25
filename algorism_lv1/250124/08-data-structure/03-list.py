# list는 가변이므로 원본이 변화함 !!
# append
my_list = [1, 2, 3]
my_list.append(4) 
print(my_list)  # 원본 변화 
print(my_list.append(4)) # append는 반환하지 않으므로

# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  

# append vs extend: extend는 리스트 형태로 담아야 함 !

# insert
my_list = [1, 2, 3]
my_list.insert(1, 5) # 인덱스 위치, 넣을 숫자 
print(my_list)  # [1, 5, 2, 3]

# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2) # 리스트에서 첫번째로 일치하는 항목 삭제 
print(my_list)  # [1, 3, 2, 2, 2]

# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(3)

print(item1) # 공백이면 제거할 마지막 항목을 반환
print(item2)  # 지정할 인덱스 항목을 반환
print(my_list) # 원본 변화


# clear: 리스트 안의 항목 전부 삭제 
my_list = [1, 2, 3]
my_list.clear() 
print(my_list)  # []

# index: 지정한 인덱스의 숫자 반환
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1

# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3

# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list.reverse())  # 반환하지 않으므로 None
print(my_list)  # [1, 3, 2, 8, 1, 9]

# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list2 = sorted(my_list, reverse = True)
print(my_list2)  # [100, 3, 2, 1]
