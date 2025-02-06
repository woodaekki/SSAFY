# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하라.
T = int(input()) # 테스트케이스 개수

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]  # 첫 원소를 최댓값으로 가정
    min_v = arr[0]  # 첫 원소를 최솟값으로 가정

    for i in range(1, N):
        if arr[i] > max_v:
            max_v = arr[i]
        if arr[i] < min_v:
            min_v = arr[i]

    print(f'#{t} {max_v - min_v}')