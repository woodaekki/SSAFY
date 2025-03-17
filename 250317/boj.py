def boj(i):
    global min_energy
    # 목적지 도달하면 반환
    if i >= n-1:
        return

    for j in range(i+1, n):
        # BOJ 순서로 잘 도는지 확인
        if (arr[i] == 'B' and arr[j] == "O") or (arr[i] == "O" and arr[j] == "J") or (arr[i] == "J" and arr[j] == "B"):
            energy = (j-i)**2 + boj(i) # 점프에너지 + 과거 든 에너지 누적
            min_energy = min(min_energy, energy) # 최소 에너지라면 갱신
    return min_energy

n = int(input())
arr = input()
min_energy = 0
boj(0)