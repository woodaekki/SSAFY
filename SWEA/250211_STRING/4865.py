def count_chars():
    str1 = input() 
    str2 = input()  
 
    dict1 = {}
    for char1 in str1:
        dict1[char1] = 0  
 
    # str2에서 str1에 포함된 문자 개수 세기
    for char2 in str2:
        if char2 in dict1:  # str1에 있는 문자만 세기
            dict1[char2] += 1
 
    # 가장 많이 등장한 문자 개수 찾기
    max_count = 0
    for count in dict1.values():
        if count > max_count:
            max_count = count
 
    return max_count
 
                 
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {count_chars()}')