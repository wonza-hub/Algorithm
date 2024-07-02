import sys
input = sys.stdin.readline

dp = [0] * 30
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 30):
    dp[i] = dp[i - 1] * i
    
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = dp[m] // (dp[n] * dp[m - n])
    print(ans)