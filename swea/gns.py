import sys
sys.stdin = open("gns.txt", "r")

def gns():
    num, cnt = map(str, input().split()) # 테스트 케이스 번호, 단어의 개수
    arr = list(input().split())

    lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    z_cnt = o_cnt = tw_cnt = th_cnt = f_cnt = fi_cnt = s_cnt = sv_cnt = e_cnt = n_cnt = 0
    for i in range(0, len(arr)):
        if arr[i] == "ZRO":
            z_cnt += 1
        elif arr[i] == "ONE":
            o_cnt += 1
        elif arr[i] == "TWO":
            tw_cnt += 1
        elif arr[i] == "THR":
            th_cnt += 1
        elif arr[i] == "FOR":
            f_cnt += 1
        elif arr[i] == "FIV":
            fi_cnt += 1
        elif arr[i] == "SIX":
            s_cnt += 1
        elif arr[i] == "SVN":
            sv_cnt += 1
        elif arr[i] == "EGT":
            e_cnt += 1
        elif arr[i] == "NIN":
            n_cnt += 1

        result = lst[0] * z_cnt + lst[1] * o_cnt + lst[2] * tw_cnt + lst[3] * th_cnt + lst[4] * f_cnt + lst[5] * fi_cnt +lst[6] * s_cnt + lst[7] * sv_cnt + lst[8] * e_cnt + lst[9] * n_cnt

        # 3글자씩 담기
        result_list = []
        for i in range(0, len(result), 3):
            result_list.append(result[i:i + 3])

    # 리스트 풀고 공백 한 칸 씩
    return " ".join(result_list)


T = int(input())
for t in range(1, T+1):
    result = gns()
    print(f'#{t}')
    print(f"{result}")

