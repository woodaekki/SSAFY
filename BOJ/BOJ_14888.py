# 계산하는 함수
def calculator(num1, num2, cal_idx):
    if cal_idx == 0:
        return num1 + num2
    elif cal_idx == 1:
        return num1 - num2
    elif cal_idx == 2:
        return num1 * num2
    elif cal_idx == 3:
        if num1 < 0:
            return -(abs(num1)//num2)
        return num1 // num2

# 재귀로 남은 연산자와 숫자 개수 세는 함수
def recur(cnt, total):
    global min_total, max_total
    if cnt == n:
        min_total = min(min_total, total)
        max_total = max(max_total, total)
        return

    for i in range(4):
        # 연산자가 1개 이상일 경우
        if cal[i] == 0:
            continue
        cal[i] -= 1
        recur(cnt+1, calculator(total, arr[cnt], i))
        cal[i] += 1

n = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))
min_total = float('inf')
max_total = float('-inf')
recur(1, arr[0])

print(max_total)
print(min_total)

