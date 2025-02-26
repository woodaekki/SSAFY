def paper(n, a, b, c, d):
    arr = [[0]*1001 for _ in range(1001)]
    for idx in range(n):
        a, b, c, d = papers[idx]
        for i in range(a, a+c):
            for j in range(b, b+d):
                arr[i][j] = idx+1 # 색종이 번호는 1번부터 시작
    
    # 각 색종이 번호의 종이 개수 셀때마다 리스트에 저장
    cnt = [0] * (n + 1)  
    for i in range(1001):
        for j in range(1001):
            cnt[arr[i][j]] += 1  
    return cnt[1:]  

n = int(input())
papers = []
for i in range(n):
    a, b, c, d = list(map(int, input().split()))
    papers.append((a, b, c, d))
result = paper(n, a, b, c, d)

for re in result:
    print(re, end = " ")