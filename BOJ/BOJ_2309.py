def dwarf():
    # 키 입력받기 
    arr = []
    for _ in range(9):
        i = int(input())
        arr.append(i)
    
    sumv = sum(arr)
    for i in range(9):
        for j in range(i+1, 9):
            if sumv - arr[i] - arr[j] == 100:
                fake1 = arr[i]
                fake2 = arr[j]
    
    # 가짜 난쟁이 2명 제외하기
    arr.remove(fake1)
    arr.remove(fake2)

    height = sorted(arr)
    return height

result = dwarf()
for re in result:
    print(re)