import sys
sys.stdin = open("2.txt", "r")

def grade(grades):
    reversed_grades = sorted(grades, reverse=True)

    j = n // 10
    # student = {'A+': 0, 'A0': 0, 'A-': 0, 'B+': 0, 'B0': 0, 'B-': 0, 'C+': 0, 'C0': 0, 'C-': 0, 'D0': 0}

    # score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] * j
    # score.sort()
    # print(score)
    # for j in range(n):
    #     student[score[j]] = reversed_grades[j]
    # print(student)

    # answer = ""
    # for key, value in student.items():
    #     if value == grades[k-1]:
    #         answer = key


T = int(input())
for t in range(1, T+1):
    n, k = list(map(int, input().split())) # 학생 수 / 학생 번호
    grades = []
    for i in range(n):
        mid, last, hw = list(map(int, input().split()))
        grades.append(mid * 0.35 + last * 0.45 + hw * 0.20)
    result = grade(grades)
    print(f'#{t} {result}')