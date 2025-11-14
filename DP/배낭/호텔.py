import sys
input=sys.stdin.readline

INF=int(1e9)
c,n=map(int,input().split())
dp=[INF]*(c+100)
dp[0]=0
for _ in range(n):
    cost,cust=map(int,input().split())
    for j in range(cust,c+100):
        dp[j]=min(dp[j],dp[j-cust]+cost)

print(min(dp[c:]))