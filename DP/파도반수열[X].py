t = int(input())

dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

for _ in range(t):
    num = int(input())
    print(dp[num])

# 복습 풀이
d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2

for i in range(6, 101):
    d[i] = d[i - 1] + d[i - 5]

for _ in range(int(input())):
    m = int(input())
    print(d[m])