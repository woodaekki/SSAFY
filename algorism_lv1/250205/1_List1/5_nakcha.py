# 박스가 쌓여있는 방을 90도 회전할때
# 낙차가 가장 큰 박스 반환

# 1. cnt = 기준 박스보다 높이가 낮은 박스의 개수
# 2. max_box = cnt가 max_box의 높이보다 높다면 (낮거나 같으면 충돌하여 떨어지지 않음)
# 3. max_box가 cnt가 된다.

# def calculate_drop_height(n, arr):
#     max_box = 0
#     for i in range(0, n): # 인덱스 에러 방지 위해 중첩 for문
#         cnt = 0
#         for j in range(i + 1, n): # i와 i+1 인덱스 비교
#             if arr[i] > arr[j]:
#                 cnt += 1
#         if cnt > max_box:
#             max_box = cnt
#     return max_box 

# drop_heights = calculate_drop_height(9, [7, 4, 2, 0, 0, 6, 0, 7, 0]) # 리스트 길이, 각 박스들의 높이
# print(drop_heights)