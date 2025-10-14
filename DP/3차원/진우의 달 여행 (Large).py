import sys
input=sys.stdin.readline

INF=int(1e6)
n,m=map(int,input().rstrip().split())
arr=[list(map(int,input().rstrip().split())) for _ in range(n)]
dp=[[[0]*3 for _ in range(m)] for _ in range(n)]
ans=INF

for j in range(m):
    for k in range(3):
        dp[0][j][k]=arr[0][j]

for i in range(1,n):
    for j in range(m):
        for k in range(3):
            # 양쪽 끝의 경우
            # 가장 좌측: 직전이 좌-우 대각선인 경우 고려 x
            # 가장 우측: 직전이 우-좌 대각선인 경우 고려 x
            if (j==0 and k==0) or (j==m-1 and k==2):
                dp[i][j][k]=INF
                continue
            if k==0:
                dp[i][j][k]=arr[i][j]+min(dp[i-1][j-1][1],dp[i-1][j-1][2])
            elif k==1:
                dp[i][j][k]=arr[i][j]+min(dp[i-1][j][0],dp[i-1][j][2])
            elif k==2:
                dp[i][j][k]=arr[i][j]+min(dp[i-1][j+1][0],dp[i-1][j+1][1])

print(min(map(min,dp[-1])))