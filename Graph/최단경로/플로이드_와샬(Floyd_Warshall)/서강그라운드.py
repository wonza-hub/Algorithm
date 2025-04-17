import sys
input=sys.stdin.readline

n,m,r=map(int,input().rstrip().split())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]
t=[0]+list(map(int,input().rstrip().split()))
ans=0

for _ in range(r):
    a,b,l=map(int,input().rstrip().split())
    graph[a][b]=l
    graph[b][a]=l

for i in range(1,n+1):
    graph[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

def item_sum(v):
    sum=0
    for i in range(1,n+1):
        if graph[v][i]<=m:
            sum+=t[i]
    return sum

for s in range(1,n+1):
    ans=max(ans,item_sum(s))

print(ans)