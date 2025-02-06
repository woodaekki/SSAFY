# <1의 자릿수를 알아내고 제거하는 연산>
# num = 456789
# counts = [0] * 12
#
# for i in range(6):
#     counts[data % 10] += 1
#     data //= 10

# ------------------------------------------------------------------
# 6자리의 숫자를 입력 받아 babygin 여부를 판단하는 프로그램을 작성하라.
# run: 3개의 숫자가 연속적인 번호를 갖는 경우
# triplet: 3개의 숫자가 동일한 번호를 갖는 경우

# 예시)
# 667767은 두개의 triplet 이므로 babygin 이다. (666, 777)
# 054060은 한개의 run과 한 개의 triplet 이므로 역시 babygin 이다. (456, 000)

# data = '444345' -> 공백없는 문자열로 입력받는 경우
# data = list(map(int, input()))
# c = [0] * 12
# print(c)

# 2. triplet 조사후 triplet 데이터 완전 삭제
i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triplet 조사
        c[i] -= 3 # 이후 삭제
        tri += 1
        continue;
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1: # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print("Baby Gin")
else:
    print("Lose")

# 입력받은 숫자를 정렬한 후, 앞뒤 3자리씩 끊어서 run 및 triplet 확인하는 방법도 !

