import sys
sys.stdin = open("str_num.txt", "r")

T = int(input())

def str_num():
    str1 = input()
    str2 = input()

    # 1. st1 딕셔너리로 만들기
    dict = {}
    for s1 in str1:
        if s1 not in dict:
            dict[s1] = 1
        else:
            dict[s1] += 1

     # 2. str2에 str1 딕셔너리 키가 있으면
    st3 = []
    for key in dict.keys():
        for s2 in str2:
            if key in s2:
                st3.append(s2)

    # 3. st3 딕셔너리로 만들기
    dict2 = {}
    for s3 in st3:
        if s3 not in dict2:
            dict2[s3] = 1
        else:
            dict2[s3] += 1

    # 4. 최빈값 찾기
    maxv = 0
    for values in dict2.values():
        if values > maxv:
            maxv = values

    return maxv


for t in range(1, T+1):
    print(f'#{t} {str_num()}')
