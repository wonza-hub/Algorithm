n=int(input())
a=list(map(int,input().split()))
dp=a.copy()
print(dp)
for i in range(1,n):
    for j in range(0,i):
        if a[j]<a[i]:
            dp[i]=max(dp[i],dp[j]+a[i])

print(max(dp))