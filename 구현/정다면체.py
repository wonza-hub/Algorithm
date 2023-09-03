n, m = map(int, input().split())
sums = [0] * (n + m + 1)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sums[i + j] += 1

max_chance = max(sums)
for i, sum in enumerate(sums):
    if sum == max_chance:
       print(i, end=" ") 