import sys
input=sys.stdin.readline

n=int(input().rstrip())
m=int(input().rstrip())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().rstrip().split())
    graph[a][b]=min(graph[a][b],c)

for s in range(1,n+1):
    graph[s][s]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==0 or j==0:
            continue
        print(0 if graph[i][j]==INF else graph[i][j],end=" ")
    print()