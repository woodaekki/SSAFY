############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 sum, len, min, max, sorted 또는 리스트 sort 메서드 사용 시 감점

def analyze_likes(weekly_like_list):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    total = 0
    max_v = -99999999999999
    min_v = 9999999999999

    # 요구 사항 1
    for likes in weekly_like_list:
        total += likes # 좋아요 합계

    # 요구사항 2
    # 가장 적은 좋아요
    for min_likes in weekly_like_list:
        if min_likes < min_v:
            min_v = min_likes
    
    # 가장 많은 좋아요 
    for max_likes in weekly_like_list:
        if max_likes > max_v:
            max_v = max_likes
    return float(total / 7), max_v - min_v # 평균, 좋아요 수 차이

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
analyze_likes([2, 5, 3, 8, 0, 10, 4])
# 1) 평균 = (2 + 5 + 3 + 8 + 0 + 10 + 4) / 7
#    = 32 / 7 ≈ 4.5714...
# 2) 최소=0, 최대=10, 차이=10
# 결과: (4.5714..., 10)
print(analyze_likes([2, 5, 3, 8, 0, 10, 4]))  # 예시: (4.5714..., 10)
print(analyze_likes([7, 7, 7, 7, 7, 7, 7]))   # (7.0, 0)

#####################################################
