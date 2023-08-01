n, w_limit = map(int, input().split())
dp = [0] * (w_limit + 1)
for _ in range(n):
    w, v = map(int, input().split())
    for j in range(w, w_limit + 1):
        dp[j] = max(dp[j], dp[j - w] + v)
print(dp[w_limit])


    