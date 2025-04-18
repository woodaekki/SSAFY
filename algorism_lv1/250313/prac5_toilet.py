people = [15, 30, 50, 10]
people.sort()
n = len(people)

total_time = 0
remain_peple = n - 1

for turn in range(n):
    time = people[turn]
    total_time += time * remain_peple
    remain_peple -= 1

print(total_time)