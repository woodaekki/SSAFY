import sys
sys.stdin = open("cnt.txt", "r")

def count_chars():
    str1 = input() 
    str2 = input()  

    dict1 = {}
    for char1 in str1:
        dict1[char1] = 0
    
    for char2 in str2:
        if char2 in dict1:
            dict1[char2] += 1
    
    max_count = 0
    for values in dict1.values():
        if values > max_count:
            max_count = values
    return max_count

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {count_chars()}')