# a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
arr = [2, 3, 7]
n = len(arr) # 원소의 개수

for i in range(2**arr): # 부분 집합의 개수
    for j in range(n): # 원소 수만큼 비교함
        if i & (1 <<,j): # i, j번의 비트가 1인 경우
            print(arr[j], end = ",") # j번 원소 출력
    print()
print()

for i in range()