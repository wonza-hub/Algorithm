import sys
input=sys.stdin.readline

n=int(input())
INF=1001
dp=[INF]*n
dp[0]=0
arr=list(map(int,input().split()))

for idx,num in enumerate(arr):
	if idx==len(arr)-1:
		break
	for j in range(idx,idx+num+1):
		if idx==j:
			continue
		if j>=len(arr):
			continue
		dp[j]=min(dp[j],dp[idx]+1)

ans=-1 if dp[-1]==INF else dp[-1]
print(ans)