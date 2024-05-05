n = int(input())
stair = [0,]
dp = [0] * (n + 1)
for _ in range(n):
    stair.append(int(input()))
    
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])
print(dp[n])

# 복습 풀이
n = int(input())
s = [0] * 301
d = [0] * 301

for i in range(1, n + 1):
    s[i] = int(input())

d[1] = s[1]
d[2] = s[1] + s[2]

for j in range(3, n + 1):
    d[j] = max(d[j - 3] + s[j - 1] + s[j], d[j - 2] + s[j])

print(d[n])

    
    