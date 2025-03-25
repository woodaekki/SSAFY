s1 = 'abc'
s2 = 'ab'
s3 = 'def'
s4 = s2 + 'c'
print(s1 == s2) # 값 비교
print(s1 is s2) # 주소 비교

print(s1 == s4)
print(s1 is s4)
print(s1 is 'abc')

print("=============")
s1 = 'ab'
s2 = 'ab'
s3 = 'ac'
s4 = 'AC'
s5 = 'abs'
print(s1 == s2)
print(s1 < s2) # 사전 순으로도 같으므로 (s1 == s2)
print(s1 < s3)
print(s3 < s4) # 대문자가 소문자보다 먼저 옴
print(ord('a'), ord('A'))
print(s1 < s5) # 길이가 짧은 문자열부터


