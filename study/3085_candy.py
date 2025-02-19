# 인접한 사탕색이 다른 두 칸을 교환한다.
# 연속된 같은 사탕 색이 몇개 있는지 확인한다.
# 기존의 최대 사탕 길이 보다 크면 그 값과 교환
# 아니면 교환한 두칸 원상복귀

def candy():
    n = int(input()) # n x n 배열
    arr = []
    for _ in range(n):
        arr.append(list(input()))
        
    max_candy = -99999999999
    for i in range(n):
        for j in range(n):
            # 가로기준, 인접한 사탕 색이 다르면 교환 
            if j+1 < n and arr[i][j] != arr[i][j+1]:
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
                # 교환 후 사탕개수가 최대인지 확인
                curr = arr[i][j]
                if curr > max_candy:
                    max_candy = curr
                else:
                    # 최대가 아니면 원상복귀 
                    arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
            
            # 세로 교환 
            if i+1 < n and arr[i][j] != arr[i+1][j]:
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                curr = arr[i][j]
                if curr > max_candy:
                    max_candy = curr 
                else:
                    # 최대가 아니면 원상복귀 
                    arr[i+1][j], arr[i][j] = arr[i][j], arr[i+1][j]

    return max_candy

print(candy())


