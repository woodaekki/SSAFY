# bit = [0, 0, 0]
# arr = [2, 3, 7]
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             s = 0
#             # print(bit) # 부분 집합에 포함된 원소 인덱스
#             for b in range(3):
#                 if bit[b] == 1:
#                     print(arr[b], end = ' ') # 부분 집합에 포함된 원소
#                     s += arr[b] # 부분 집합에 포함된 원소의 합
#             print(bit, s)

arr = [2, 3, 7]
n = len(arr) # 원소의 개수

for i in range(1<<n): # 부분 집합의 개수
    for j in range(n): # 원소 수만큼 비교함
        if i & (1 <<,j): # i, j번의 비트가 1인 경우
            print(arr[j], end = ",") # j번 원소 출력
    print()
print()


