n = int(input())
stones = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = stones[0][0]

for i in range(n):
    for j in range(n):
        if i == 0 and j > 0:
            dp[i][j] = dp[i][j - 1] + stones[i][j]
        if i > 0 and j == 0:
            dp[i][j] = dp[i - 1][j] + stones[i][j]
        elif i > 0 and j > 0:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + stones[i][j]
    
print(dp[n - 1][n - 1])