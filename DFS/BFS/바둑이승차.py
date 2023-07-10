c, n = map(int, input().split())
dogs = []
total_weight = 0
for _ in range(n):
    dog_weight = int(input())
    dogs.append(dog_weight)
    total_weight += dog_weight
answer = -1


def dfs(i, sum, asif_sum):
    global answer
    if sum + (total_weight - asif_sum) < answer:
        return
    if sum > c:
        return
    if i == n:
        if sum > answer:
            answer = max(answer, sum)
    else:
        dfs(i + 1, sum + dogs[i], asif_sum + dogs[i])
        dfs(i + 1, sum, asif_sum + dogs[i])


dfs(0, 0, 0)
print(answer)