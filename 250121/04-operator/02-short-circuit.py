# 단축 평가

vowels = 'aeiou'

print(('a' and 'b') in vowels)  #False -> print(('a' and 'b')는 최종 'b'만 출력, vowels안에 없으니 False
print(('b' and 'a') in vowels)  #True

#두 값이 모두 참이면 2번째 값, 그렇지 않으면 1번째 값 반환
print(3 and 5)  #5
print(3 and 0)  #0
print(0 and 3)  #0 -> 0은 거짓, 1은 참으로 간주 
print(0 and 0)  #0 -> 앞의 0

#왼쪽 값이 참이면 왼쪽 값을 반환하고, 그렇지 않으면 오른쪽 값을 반환
print(5 or 3)  #5
print(3 or 0)  #3
print(0 or 3)  #3
print(0 or 0)  #0
