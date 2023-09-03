n = int(input())
scores = list(map(int, input().split()))
avg = int(sum(scores) / n + 0.5)
min_diff = 10e9
ans = 1

for idx, score in enumerate(scores):
    diff = abs(score - avg)
    if diff < min_diff:
        min_diff = diff
        closet_score = score
        ans = idx + 1
    elif diff == min_diff:
        if score > closet_score:
            closet_score = score
            ans = idx + 1

print(avg, ans, end=" ")
        