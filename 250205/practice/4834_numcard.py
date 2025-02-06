T = int(input())

for t in range(1, T + 1):
    n = int(input()) # 카드 장수
    # 공백없이 연속된 숫자를 입력받을 때 !!
    arr = input()
    
    count_dict = {}
    # 1. arr 리스트를 순회하며 새로 등장하는 숫자마다 키로 입력한다.
    # 이미 있는 키이면 += 1 한다.
    for num in arr:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    
    # 2. 딕셔너리 내의 가장 많은 등장 횟수 키, 그 장 수 찾기
    max_cnt = 0
    max_num = 0
    for keys, values in count_dict.items():
        if values > max_cnt:
            max_cnt = values
            max_num = keys
        # 3. 동일한 횟수일 때, 더 큰 숫자를 선택
        if values == max_cnt:
            if keys > max_num: 
                max_num = keys
    print(f'#{t} {max_num} {max_cnt}')