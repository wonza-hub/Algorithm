import sys
input=sys.stdin.readline
import heapq as hq

n,k=map(int,input().rstrip().split())
# w의 최댓값: 20
arr=[[0]*k for _ in range((20*(n//k+1))+1)]
idx=0
q=[]
for i in range(k):
    hq.heappush(q,[0,i])
for _ in range(n):
    id,w=map(int,input().rstrip().split())
    [w_sum,idx]=hq.heappop(q)
    hq.heappush(q,[w_sum+w,idx])
    arr[0][idx]=w_sum+w
    arr[arr[0][idx]][idx]=id

N=1
ans=0
for i in range(1,len(arr)):
    for j in range(k-1,-1,-1):
        if arr[i][j]:
            ans+=arr[i][j]*N
            N+=1
print(ans)
