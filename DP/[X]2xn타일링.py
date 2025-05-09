# 백준
n = int(input())
dp = [0] * 1001

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)

# 프로그래머스
def solution(n):
    d=[0]*(n+1)
    d[1],d[2]=1,2
    for i in range(3,n+1):
        d[i]=(d[i-1]+d[i-2])%1000000007
        
    return d[n]