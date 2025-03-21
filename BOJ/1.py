# 계란으로 계란치기
# 어려워서 지선생님께 간간히 여쭤보았습니다.
# 하지만 답이 안나옵니다.

# 계란으로 계란치기
# 어려워서 지선생님께 간간히 여쭤보았습니다.
# 하지만 답이 안나옵니다.

def egg(idx):
    global max_cnt, dura, wei

    # 다 치면 깨진 최대 계란 개수 구하고 종료
    if idx == n:
        cnt = 0
        for j in range(n):
            # 둘 중 깨진 계란 있으면 카운트 증가
            if dura[j] <= 0:
                cnt += 1

        max_cnt = max(max_cnt, cnt)
        return

    # 계란 깨지면 다음 계란으로
    egg_under = dura[:idx] + dura[idx+1:]

    if dura[idx] <= 0 or len([x for x in egg_under if x > 0]) == 0:
        egg(idx + 1)
        return

    for i in range(n):
        if idx == i or dura[i] <= 0:  # 자신끼리 치지 않도록
            continue

        # 내구도 만큼 깨기
        dura[i] -= wei[idx]
        dura[idx] -= wei[i]

        egg(idx + 1)

        # 원복
        dura[i] += wei[idx]
        dura[idx] += wei[i]


n = int(input())
dura = []
wei = []
for _ in range(n):
    durability, weight = list(map(int, input().split()))
    dura.append(durability)
    wei.append(weight)

max_cnt = 0

egg(0)
print(max_cnt)