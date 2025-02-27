from collections import deque
import sys
input=sys.stdin.readline

n=int(input().rstrip())
graph=[[] for _ in range(n+1)]
time=[0]*(n+1)
ind=[0]*(n+1)

for i in range(1,n+1):
    tmp=list(map(int,input().rstrip().split()))
    time[i]=tmp[0]
    ind[i]=tmp[1]
    for j in tmp[2:]:
        graph[j].append(i)

def topology_sort():
    d=time.copy()
    q=deque()

    for i in range(1,n+1):
        if ind[i]==0:
            q.append(i)

    while q:
        now=q.popleft()
        for v in graph[now]:
            d[v]=max(d[v],d[now]+time[v])
            ind[v]-=1
            if ind[v]==0:
                q.append(v)

    return max(d)

ans=topology_sort()
print(ans)