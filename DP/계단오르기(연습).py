n = int(input())
dp = [0] * (n + 1)

def dfs(step):
    if dp[step] > 0:
        return dp[step]
    if step == 1 or step == 2:
        return step
    dp[step] = dfs(step - 1) + dfs(step - 2)
    return dp[step]
    
print(dfs(n))