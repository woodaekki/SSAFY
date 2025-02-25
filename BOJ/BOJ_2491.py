def permu():
    n = int(input())
    arr = list(map(int, input().split()))

    maxv1 = -99999999999999
    maxv2 = -999999999999999
    cnt1 = cnt2 = 1

    # 연속해서 증가하는 경우
    for i in range(0, n):
        if 0 <= i+1 < n and arr[i] <= arr[i+1]: 
            cnt1 += 1
        else:
            if cnt1 > maxv1:
                maxv1 = cnt1
            cnt1 = 1
    
    # 연속해서 감소하는 경우
    for j in range(0, n):
        if 0 <= j+1 < n and arr[j] >= arr[j+1]: 
            cnt2 += 1
        else:
            if cnt2 > maxv2:
                maxv2 = cnt2
            cnt2 = 1
    
    result = max(maxv1, maxv2)
    return result
print(permu())
        
  
