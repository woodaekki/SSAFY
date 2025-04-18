import sys
sys.stdin = open("2.txt", "r")

def grade(grades):
    origin = []
    # 원본 학생의 인덱스 번호와 점수 저장하기 
    for idx in range(n):
        origin.append((idx+1, grades[idx])) # 학생 번호는 1번부터!

    # 총점 정렬하기 
    total = sorted(origin, key=lambda x: x[1], reverse=True) # 총점을 기준으로 정렬렬 
    # print(total)
    score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    score_ratio = n // 10
    
    # 각 등급을 score_ratio만큼 늘리기 
    expanded_scores = []
    for sc in score:
        expanded_scores += [sc] * score_ratio
    # print(expanded_scores)
    
    # 학생들에게 성적 부여하기
    student_grades = {}
    for i in range(n):
        student_grades[total[i][0]] = expanded_scores[i]
    # print(student_grades)
    # k번 학생의 학점 반환
    return student_grades[k]

T = int(input())
for t in range(1, T+1):
    n, k = list(map(int, input().split())) # 학생 수 / 학생 번호
    grades = []
    for i in range(n):
        mid, last, hw = list(map(int, input().split()))
        grades.append(mid * 0.35 + last * 0.45 + hw * 0.20)
    result = grade(grades)
    print(f'#{t} {result}')