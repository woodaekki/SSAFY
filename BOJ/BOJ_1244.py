def switch():
    n = int(input())
    arr = list(map(int, input().split()))
    num = int(input())

    for _ in range(num):
        j, k = list(map(int, input().split()))

        # 남자인 경우
        if j == 1:
            for i in range(k-1, n, k):
                arr[i] = 1 - arr[i]
        
        # 여자인 경우
        if j == 2:
            # 자기 자신은 무조건 반대로 바꾸기 
            arr[k-1] = 1 - arr[k-1]
            for m in range(1, n):
                # 대칭이 같은 수일 경우 반대로 바꾸기
                if 0 <= k-1-m < n and 0 <= k-1+m < n and arr[k-1-m] == arr[k-1+m]:
                    arr[k-1-m] = 1 - arr[k-1-m]
                    arr[k-1+m] = 1 - arr[k-1+m]
                else:
                    break
    return arr

result = switch()

# 한줄에 20개씩 출력 
for i in range(0, len(result), 20):
    print(*result[i:i+20])  
