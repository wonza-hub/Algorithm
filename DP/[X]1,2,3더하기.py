n = int(input())
dp = [0] * 12

dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(n):
    print(dp[int(input())])

# 복습 풀이
# dp[i]: i를 1,2,3의 합으로 나타내는 경우의 수
dp=[0]*12
dp[1]=1
dp[2]=2
dp[3]=4

n=int(input())
for i in range(4,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    
for _ in range(n):
    print(dp[int(input())])