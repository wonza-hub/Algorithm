from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
graph=[[] for _ in range(n+1)]
ind=[0]*(n+1)
ch=[0]*(n+1)

for _ in range(m):
    tmp=list(map(int,input().rstrip().split()))
    k,arr=tmp[0],tmp[1:]
    for i in range(1,len(arr)):
        graph[arr[i-1]].append(arr[i])
        ind[arr[i]]+=1

q=deque()
for i in range(1,n+1):
    if ind[i]==0:
        q.append(i)

res=[]
while q:
    x=q.popleft()
    if ch[x]:
        break
    res.append(x)
    for v in graph[x]:
        ind[v]-=1
        if ind[v]==0:
            q.append(v)

if len(res)==n:
    for i in res:
        print(i)
else:
    print(0)
