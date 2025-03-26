import sys
sys.stdin = open("jungsik.txt", "r")

def bank():
    # 2진수에서 한자리만 바꾼 리스트들 생성 
    two_lst = [0, 1]
    two_change = []  
    for i in range(len(two)):
        copy_two = list(two)
        ori_two = copy_two[i]
        for two_l in two_lst:
            if ori_two != two_l:
                copy_two[i] = two_l
                # 2진수를 10진수로 
                deci = 0
                for tw in copy_two:
                    deci = deci * 2 + tw
                    # print(deci)
                two_change.append(deci)  
                # 다시 원래 상태로 
                copy_two[i] = ori_two
    
    # 3진수에서 한자리만 바꾼 리스트들 생성 
    three_lst = [0, 1, 2]
    three_change = []
    for j in range(len(three)):
        copy_three = list(three)
        ori_three = copy_three[j]
        for three_l in three_lst:
            if ori_three != three_l:
                copy_three[j] = three_l
                # 3진수를 10진수로 변환
                deci2 = 0
                for thr in copy_three:
                    deci2 = deci2 * 3 + thr
                    # print(deci2)
                three_change.append(deci2)
                # 원상태로
                copy_three[j] = ori_three
    
    # 공통된 값 찾기 
    for common in two_change:  
        if common in three_change:
            return common
    

T = int(input())
for t in range(1, T+1):
    two = list(map(int, input()))
    three = list(map(int, input()))
    result = bank()
    print(f'#{t} {result}')