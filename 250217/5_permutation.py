def powerset(k, curS):

    # 합이 5 넘으면 반환
    if curS > 5:
        return

    # 합이 5인 경우, 부분집합과 그 합 출력 
    if curS == 5:
        print(result, curS)
        return

    # 배열 끝에 도착하면 반환 
    if k==N:
        return

    # 현재 원소 부분집합에 포함(포함은 1로 표시)
    result[k] = 1
    powerset(k+1, curS+arr[k]) # 재귀 호출 

    # 현재 원소 부분집합에 제외(비포함은 0으으로 표시)
    result[k] = 0
    powerset(k+1, curS) # 현재 원소 제외하고 재귀 호출

#=======================================================
# def per_1(k):
#     if k==N:
#         print(result)
#         return

#     candidates = []
#     for i in range(N):
#         if i not in result[0:k]:
#             candidates.append(i)

#     for i in candidates:
#         result[k] = i
#         per(k+1)


#======================================================
# visited를 이용한 순열 생성 함수 
def per(k):
    if k==N:
        print(result)
        return

    for i in range(N):
        if not visited[i]: # 방문 안했으면 방문처리하기 
            result[k] = i # k번째 자리에 i를 방문 
            visited[i] = True
            per(k+1) # 다음인 k+1번째로 이동하여 재귀호출
            visited[i] = False # 방문 표시 원상복귀 

N = 3
arr = [1, 2, 3]

result = [-1] * N

# powerset(0, 0)
visited = [False] * N
per(0)