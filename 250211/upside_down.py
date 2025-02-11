s = "reverse this strings"
s = s[::-1]
print(s)

txt = ['a','b','c','d','e']
n = len(txt)
for i in range(n//2):
    txt[i], txt[n-1-i] = txt[n-1-i], txt[i] # 절반을 기준으로 처음과 마지막, 2번째와 뒤에서 2번째.. 교환
print(txt)

s = 'abcd'
s = list(s)
s.reverse()
s = "".join(s)
print(s)