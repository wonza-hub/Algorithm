import sys
input = sys.stdin.readline

n, k = map(int, input().split())
weight = [0] * (n + 1)
value = [0] * (n + 1)
for i in range(1, n + 1):
    weight[i], value[i] = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

for cur in range(1, n + 1):
    for limit in range(1, k + 1):
        if weight[cur] <= limit:
            dp[cur][limit] = max(dp[cur - 1][limit], dp[cur - 1][limit - weight[cur]] + value[cur])
        else:
            dp[cur][limit] = dp[cur - 1][limit]

print(dp[-1][-1])
    