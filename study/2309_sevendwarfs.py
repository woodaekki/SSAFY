# 입력받기
arr = []
for i in range(0, 9):
    num = int(input())
    arr.append(num) 

# 총합에서 가짜 난쟁이 2명 걸러내기
# 합이 100이 되도록
sumv = 0
for l in range(0, 9):
    sumv += arr[l]

for n in range(0, 8):
    for m in range(n+1, 9):
        if sumv - arr[n] -arr[m] == 100:
            fake1 = arr[n]
            fake2 = arr[m]

# 가짜 제거하기
arr.remove(fake1)
arr.remove(fake2)
for ar in sorted(arr):
    print(ar)
    
