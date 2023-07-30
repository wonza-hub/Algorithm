n = int(input())
bricks = []

for _ in range(n):
    wth, hth, w = map(int, input().split())
    bricks.append((wth, hth, w))
bricks.sort(reverse = True)

dp = [0] * n
dp[0] = bricks[0][1]
res = bricks[0][1]

for i in range(1, n):
    max_hth = 0
    for j in range(0, i):
        if bricks[j][2] > bricks[i][2] and dp[j] > max_hth:
            max_hth = dp[j]
    dp[i] = max_hth + bricks[i][1]
    res = max(res, dp[i])

print(res)