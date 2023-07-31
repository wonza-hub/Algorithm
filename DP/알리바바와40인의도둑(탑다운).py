n = int(input())
stones = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = stones[0][0]


def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    if x == 0 and y == 0:
        return dp[0][0]
    else:
        if x == 0:
            dp[x][y] = dfs(x, y - 1) + stones[x][y]
        elif y == 0:
            dp[x][y] = dfs(x - 1, y) + stones[x][y]
        else:
            dp[x][y] = min(dfs(x, y - 1), dfs(x - 1, y)) + stones[x][y]
        return dp[x][y]


print(dfs(n - 1, n - 1))
