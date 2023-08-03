# 2차원 리스트 구현
# n, m = map(int,input().split())
# dp = [[0] * (m + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     dp[i] = dp[i - 1].copy()
#     score, time = map(int, input().split())
#     for j in range(time, m + 1):
#         dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time] + score)
# print(dp[n][m])

# 1차원 리스트 구현
n, m = map(int,input().split())
dp = [0] * (m + 1)

for _ in range(n):
    score, time = map(int, input().split())
    for i in range(m, time - 1, -1):
        dp[i] = max(dp[i], dp[i - time] + score)
print(dp[m])