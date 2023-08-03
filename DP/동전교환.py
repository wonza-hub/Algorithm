n = int(input())
coins = list(map(int, input().split()))
coins.sort()
exch = int(input())
dp = [501] * (exch + 1)
dp[0] = 0
for coin in coins:
    for i in range(coin, exch + 1):
        dp[i] = min(dp[i], dp[i -coin] + 1)

print(dp[-1])
    