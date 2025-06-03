def diff():
    str1 = input()
    str2 = input()
  
    if str1 in str2:
        return 1
    else:
        return 0
  
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {diff()}')