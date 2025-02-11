a, b = list(map(int, input().split()))
min = int(input())

lft = (b+min) // 60 # 몫
lft2 = (b+min) % 60 # 나머지
if b+min < 60:
    a += lft
    b += lft2

elif b+min == 60:
    a += lft
    b += lft2

else:
    a += lft
    b += lft2


print(f'{a} {b}')
