n = int(input())
ox = list(map(int, input().split()))
scores = [0] * n

if ox[0] == 0:
    scores[0] = 0
else:
    scores[0] = 1

for i in range(1, n):
    if ox[i] == 0:
        scores[i] = 0
    else:
        if ox[i - 1] == 1:
            scores[i] = scores[i - 1] + 1
        else:
            scores[i] = 1

print(sum(scores))

# 간결한 풀이
n = int(input())
ox = list(map(int, input().split()))
sum = 0
cnt = 0
for x in ox:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)
